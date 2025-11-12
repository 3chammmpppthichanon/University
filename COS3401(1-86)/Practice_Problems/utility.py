# numpy
# matplotlib
# opencv-python

from typing import Any

import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image_plt(img: Any, *, title: str = '', gray: bool = False) -> None:
    """แสดงภาพด้วย Matplotlib (เหมาะสำหรับ Jupyter Notebook)"""
    plt.axis('off')
    plt.imshow(img, cmap='gray' if gray else None)
    if title:
        plt.title(title)
    plt.show()

def show_image_cv2(img: cv2.typing.MatLike, *, title: str = '') -> None:
    """แสดงภาพด้วยหน้าต่างของ OpenCV (เหมาะสำหรับรันสคริปต์ .py)"""
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def apply_gamma_correction(img: cv2.typing.MatLike, gamma: float, *, c: float = 255.0) -> cv2.typing.MatLike:
    """ปรับความสว่างของภาพด้วย Power-Law (Gamma) Transformation (s = c*r^gamma)"""
    # สร้างตาราง lookup table (LUT) สำหรับค่า gamma
    table = np.array([i / 255.0 for i in range(256)])
    
    gamma_lut = c * (table**gamma)
    gamma_lut = gamma_lut.astype(np.uint8)
    
    # ใช้ LUT กับภาพที่ผ่านการ normalize แล้ว
    return cv2.LUT(normalize_contrast(img), gamma_lut)

def normalize_contrast(img: cv2.typing.MatLike) -> cv2.typing.MatLike:
    """ยืด Contrast ของภาพให้อยู่ในช่วง 0-255 (Min-Max Normalization)"""
    img = img.astype(np.float32)
    img = (img - img.min()) / (img.max() - img.min()) * 255
    return img.astype(np.uint8)


def reduce_saturation(img_hsv: cv2.typing.MatLike, percent: float) -> cv2.typing.MatLike:
    """ลดความอิ่มตัวของสี (Saturation) ของภาพในระบบสี HSV"""
    img_hsv = img_hsv.astype(np.float32)
    # (h: 0, s: 1, v: 2)
    # ลดค่า Saturation (channel ที่ 1) ตาม 'percent'
    img_hsv[:, :, 1] *= percent  # type: ignore
    return img_hsv.astype(np.uint8)


# --- Color Space ---


def bgr_to_cmyk(image_bgr: cv2.typing.MatLike) -> cv2.typing.MatLike:
    """แปลงภาพ BGR (OpenCV) เป็น CMYK"""
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    
    rgb_norm = image_rgb / 255.0

    R = rgb_norm[:, :, 0]
    G = rgb_norm[:, :, 1]
    B = rgb_norm[:, :, 2]

    # Calculate the CMY values
    C = 1 - R
    M = 1 - G
    Y = 1 - B

    K = np.minimum(np.minimum(C, M), Y)

    denominator = 1 - K
    # ป้องกันการหารด้วย 0
    denominator[denominator == 0] = 1

    C = (C - K) / denominator
    M = (M - K) / denominator
    Y = (Y - K) / denominator

    cmyk_image = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    return cmyk_image


def cmyk_to_rgb(cmyk_image: cv2.typing.MatLike) -> cv2.typing.MatLike:
    """แปลงภาพ CMYK เป็น RGB"""
    C = cmyk_image[:, :, 0] / 255.0
    M = cmyk_image[:, :, 1] / 255.0
    Y = cmyk_image[:, :, 2] / 255.0
    K = cmyk_image[:, :, 3] / 255.0

    R = 255 * (1 - C) * (1 - K)
    G = 255 * (1 - M) * (1 - K)
    B = 255 * (1 - Y) * (1 - K)

    rgb_image = np.dstack((R, G, B)).astype(np.uint8)
    return rgb_image

def bgr_to_cmyk_channels(
    img_bgr: cv2.typing.MatLike,  # CHANGED: 'img' -> 'img_bgr'
    rgb_scale: float = 255.0,
    cmyk_scale: float = 255.0,
) -> tuple[
    cv2.typing.MatLike,
    cv2.typing.MatLike,
    cv2.typing.MatLike,
    cv2.typing.MatLike,
]:
    """แปลงภาพ BGR เป็น 4 Channels (C, M, Y, K) แยกกัน"""
    # R คือ channel 2, G คือ 1, B คือ 0 ใน BGR
    R = img_bgr[:, :, 2].astype(np.float16) / rgb_scale
    G = img_bgr[:, :, 1].astype(np.float16) / rgb_scale
    B = img_bgr[:, :, 0].astype(np.float16) / rgb_scale

    C, M, Y = 1 - R, 1 - G, 1 - B
    K = np.minimum.reduce([C, M, Y])

    C = (C - K) * cmyk_scale
    M = (M - K) * cmyk_scale
    Y = (Y - K) * cmyk_scale
    K = K * cmyk_scale

    return C.astype(np.uint8), M.astype(np.uint8), Y.astype(np.uint8), K.astype(np.uint8)


# --- Thresholding ---

def _calculate_intermean_step(hist_data: cv2.typing.MatLike, current_thresh: int, start: int, end: int) -> int:
    """(ฟังก์ชันช่วย) คำนวณค่าเฉลี่ยของ 2 กลุ่ม (background/foreground)"""

    prob = np.zeros_like(hist_data, dtype=np.float16)
    total = np.sum(hist_data[start:end])
    prob[start:end] = hist_data[start:end] / total

    weight_bg = np.sum(prob[start:current_thresh]) + 0.0000001

    weight_fg = (1 - weight_bg) + +0.0000001

    indices_bg = np.array(list(range(start, current_thresh)))
    indices_fg = np.array(list(range(current_thresh, end)))


    mean_bg = np.sum(indices_bg * prob[start:current_thresh]) / weight_bg
    mean_fg = np.sum(indices_fg * prob[current_thresh:end]) / weight_fg

    if mean_bg == 0.0:
        new_thresh = mean_fg
    elif mean_fg == 0.0:
        new_thresh = mean_bg
    else:
        new_thresh = (mean_bg + mean_fg) / 2

    return new_thresh.astype(np.int16)  # type: ignore


def apply_threshold(img: cv2.typing.MatLike, thresh_value: int | None = None, inverse: bool = False) -> cv2.typing.MatLike:
    """สร้างภาพไบนารี (ขาว/ดำ) จากค่า threshold ที่กำหนด"""

    result = np.zeros_like(img, dtype=np.uint8)
    
    # ถ้าไม่กำหนด 'thresh_value' มา, จะใช้ค่าเฉลี่ยของภาพแทน
    thresh_value = thresh_value or int(np.mean(img))  # type: ignore
    
    if inverse:
        # Inverse: ต่ำกว่า thresh เป็น 255 (ขาว), สูงกว่าเป็น 0 (ดำ)
        result[img <= thresh_value] = 255
    else:
        # Normal: สูงกว่า thresh เป็น 255 (ขาว), ต่ำกว่าเป็น 0 (ดำ)
        result[img >= thresh_value] = 255
    return result

def calculate_histogram(img: cv2.typing.MatLike) -> cv2.typing.MatLike:
    """คำนวณ Histogram ของภาพ Grayscale ด้วยตัวเอง (manual)"""
    row, col = img.shape
    hist = [0.0] * 256
    for i in range(row):
        for j in range(col):
            hist[img[i, j]] += 1
    return np.array(hist)


def show_histogram(hist_data: cv2.typing.MatLike, show_axis: bool) -> None:
    """แสดงผลกราฟ Histogram ด้วย Matplotlib"""
    plt.figure(figsize=(4, 2))
    plt.plot(hist_data)
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    if show_axis:
        plt.axis('on')
    else:
        plt.axis('off')
    plt.show()

def find_intermean_threshold(
    img: cv2.typing.MatLike,
    *,
    tolerance: int = 1,
    num_levels: int = 3,
) -> tuple[cv2.typing.MatLike, int]:
    """ค้นหาค่า threshold ด้วยวิธี Intermean แบบวนซ้ำ (Iterative)"""
    hist = calculate_histogram(img)

    start, end = 0, 256
    final_thresh = 0

    # ลูป 'num_levels' นี้ดูเหมือนจะพยายามหา K-level thresholding
    # แต่โค้ดคืนค่าแค่ threshold สุดท้าย
    for _ in range(num_levels):
        thresh_old = int((start + end) * 0.5)
        threshold_history = [thresh_old]

        while True:
            # CHANGED: 't1' -> 'thresh_new'
            thresh_new = _calculate_intermean_step(hist, thresh_old, start, end) # CHANGED
            threshold_history.append(thresh_new)
            
            # วนจนกว่าค่า threshold จะนิ่ง (ต่างกันไม่เกิน tolerance)
            if abs(thresh_new - thresh_old) < tolerance:
                break
            thresh_old = thresh_new

        final_thresh = threshold_history[-1]
        # อัปเดต 'start' สำหรับการวนรอบถัดไป (เพื่อหา level ต่อไป)
        start = final_thresh + 1

    # สร้างภาพไบนารีด้วยค่า threshold สุดท้ายที่หาได้
    _, binary_img = cv2.threshold(img, final_thresh, 255, cv2.THRESH_BINARY)
    return binary_img, final_thresh

def find_otsu_threshold(hist_data: cv2.typing.MatLike, start: int, end: int) -> int:
    """ค้นหาค่า threshold ที่ดีที่สุดด้วยวิธี Otsu"""
    prob = np.zeros_like(hist_data, dtype='float16')
    total = np.sum(hist_data[start:end])
    prob[start:end] = hist_data[start:end] / total

    max_variance = -1
    best_threshold = -1

    for t in range(start + 1, end - 1):
        weight_bg = np.sum(prob[start:t]) + 0.00000001
        weight_fg = np.sum(prob[t:end]) + 0.00000001

        indices_bg = np.array(list(range(start, t)))
        indices_fg = np.array(list(range(t, end)))

        mean_bg = np.sum(indices_bg * prob[start:t]) / weight_bg
        mean_fg = np.sum(indices_fg * prob[t:end]) / weight_fg

        variance = (weight_bg * weight_fg) * np.power(mean_bg - mean_fg, 2)
        
        if variance > max_variance:
            max_variance = variance
            best_threshold = t

    return best_threshold

# (Mask นี้คือ Sobel (k=2) หรือ Prewitt (k=1))
def apply_sobel_prewitt_edge(img: cv2.typing.MatLike, k_weight: int) -> cv2.typing.MatLike:
    """ตรวจจับขอบภาพด้วย General Sobel/Prewitt Operator"""
    img_float = img.copy().astype(np.float32)
    out = np.zeros_like(img, dtype=np.float32)
    
    mask_gx = np.array(
        [
            [-1, 0, 1],
            [-k_weight, 0, k_weight],
            [-1, 0, 1],
        ],
        dtype='float16',
    )
    mask_gy = np.array(
        [
            [-1, -k_weight, -1],
            [0, 0, 0],
            [1, k_weight, 1],
        ],
        dtype='float16',
    )
    

    kernel_size, _ = mask_gx.shape
    border = kernel_size // 2
    (height, width) = img_float.shape
    
    for i in range(border, height - border):
        for j in range(border, width - border):
            gx, gy = 0.0, 0.0
            image_window = img_float[i - border : i + border + 1, j - border : j + border + 1]
            
            # Convolution
            gx = np.multiply(image_window, mask_gx).sum()
            gy = np.multiply(image_window, mask_gy).sum()
            
            # Magnitude
            out[i, j] = np.sqrt(gx**2 + gy**2)
            
    out[out > 255.0] = 255.0
    return out.astype(np.uint8)

def merge_quarters(
    img: cv2.typing.MatLike,
    top_left: cv2.typing.MatLike,     # CHANGED: 'sub11'
    bottom_left: cv2.typing.MatLike,  # CHANGED: 'sub12'
    top_right: cv2.typing.MatLike,    # CHANGED: 'sub21'
    bottom_right: cv2.typing.MatLike, # CHANGED: 'sub22'
) -> cv2.typing.MatLike:
    """รวม 4 ภาพย่อย (quarters) กลับเป็นภาพใหญ่ 1 ภาพ"""
    out = np.zeros_like(img, dtype='uint8')
    h, w = img.shape
    
    half_width, half_height = w // 2, h // 2
    
    out[:half_height, :half_width] = top_left
    out[half_height:, :half_width] = bottom_left
    out[:half_height, half_width:] = top_right
    out[half_height:, half_width:] = bottom_right

    return out

# (ฟังก์ชันช่วยสำหรับแบ่งครึ่งแนวตั้ง, ใส่ _ เพื่อบอกว่าเป็น internal)
def _split_image_vertical(img: cv2.typing.MatLike) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike]:
    """(ฟังก์ชันช่วย) แบ่งภาพครึ่งซ้าย-ขวา"""
    _, w = img.shape
    w_cutoff = w // 2
    img_left = img[:, :w_cutoff]
    img_right = img[:, w_cutoff:]
    return img_left, img_right

def split_image_quarters(
    img: cv2.typing.MatLike,
) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]:
    """แบ่งภาพ 1 ภาพ ออกเป็น 4 ภาพย่อย (quarters)"""
    
    left_half, right_half = _split_image_vertical(img) # CHANGED

    # วิธีการแบ่งโดยใช้ transpose นี้ค่อนข้างซับซ้อน
    # แต่ผลลัพธ์คือการแบ่งครึ่งแนวนอน
    
    # แบ่งครึ่งซ้าย (left_half) ออกเป็น บน-ล่าง
    top_left_T, bottom_left_T = _split_image_vertical(left_half.transpose()) # CHANGED
    
    # แบ่งครึ่งขวา (right_half) ออกเป็น บน-ล่าง
    top_right_T, bottom_right_T = _split_image_vertical(right_half.transpose()) # CHANGED

    # Transpose กลับคืน
    top_left = top_left_T.transpose()
    bottom_left = bottom_left_T.transpose()
    top_right = top_right_T.transpose()
    bottom_right = bottom_right_T.transpose()

    return top_left, bottom_left, top_right, bottom_right