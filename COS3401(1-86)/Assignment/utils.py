from typing import Any
import cv2
import matplotlib.pyplot as plt
import numpy as np


def plt_image(img: Any, *, title: str = '', gray: bool = False) -> None:
    plt.axis('off')
    plt.imshow(img, cmap='gray' if gray else None)
    if title:
        plt.title(title)
    plt.show()

def show_plots(img1: Any, img2: Any, title1="Image 1", title2="Image 2"):
    plt.figure(figsize=(10, 5))

    # ภาพที่ 1
    plt.subplot(1, 2, 1)
    if len(img1.shape) == 2:  
        plt.imshow(img1, cmap='gray')
    else:
        plt.imshow(img1)
    plt.title(title1)
    plt.axis('off')

    # ภาพที่ 2 ตรวจสอบว่าเป็น Grayscale หรือไม่ เพื่อกำหนด cmap
    plt.subplot(1, 2, 2)
    if len(img2.shape) == 2:
        plt.imshow(img2, cmap='gray')
    else:
        plt.imshow(img2)
        
    plt.title(title2)
    plt.axis('off')

    plt.show()

def show_plots_3(img1: Any, img2: Any, img3: Any,
    title1: str = "Image 1", 
    title2: str = "Image 2", 
    title3: str = "Image 3"):
    
    plt.figure(figsize=(15, 5))

    # ภาพที่ 1
    plt.subplot(1, 3, 1)
    if len(img1.shape) == 2:
        plt.imshow(img1, cmap='gray')
    else:
        plt.imshow(img1)
    plt.title(title1)
    plt.axis('off')

    #ภาพที่ 2
    plt.subplot(1, 3, 2)
    if len(img2.shape) == 2:
        plt.imshow(img2, cmap='gray')
    else:
        plt.imshow(img2)
    plt.title(title2)
    plt.axis('off')

    #ภาพที่ 3
    plt.subplot(1, 3, 3)
    if len(img3.shape) == 2:
        plt.imshow(img3, cmap='gray')
    else:
        plt.imshow(img3)
    plt.title(title3)
    plt.axis('off')
    
    #plt.tight_layout() # ช่วยจัด layout ให้สวยงาม ไม่ทับซ้อนกัน
    plt.show()

def cv_show(img: cv2.typing.MatLike, *, title: str = '') -> None:
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def power_gamma(img: cv2.typing.MatLike, gamma: float, *, c: float = 255.0) -> cv2.typing.MatLike:
    table = np.array([i / 255.0 for i in range(256)])
    gam_table = c * (table**gamma)
    gam_table = gam_table.astype(np.uint8)
    return cv2.LUT(normalize(img), gam_table)


def normalize(img: cv2.typing.MatLike) -> cv2.typing.MatLike:
    img = img.astype(np.float32)
    img = (img - img.min()) / (img.max() - img.min()) * 255
    return img.astype(np.uint8)


def reduce_saturation(img_hsv: cv2.typing.MatLike, percent: float) -> cv2.typing.MatLike:
    img_hsv = img_hsv.astype(np.float32)
    # (h: 0, s: 1, v: 2)
    img_hsv[:, :, 1] *= percent  # type: ignore
    return img_hsv.astype(np.uint8)


# color space


def rgb_to_cmyk(image: cv2.typing.MatLike) -> cv2.typing.MatLike:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb_normalized = rgb_image / 255.0

    R = rgb_normalized[:, :, 0]
    G = rgb_normalized[:, :, 1]
    B = rgb_normalized[:, :, 2]

    # Calculate the CMY values
    C = 1 - R
    M = 1 - G
    Y = 1 - B

    K = np.minimum(np.minimum(C, M), Y)

    denominator = 1 - K
    denominator[denominator == 0] = 1

    C = (C - K) / denominator
    M = (M - K) / denominator
    Y = (Y - K) / denominator

    cmyk_image = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)

    return cmyk_image


def cmyk_to_rgb(cmyk_image: cv2.typing.MatLike) -> cv2.typing.MatLike:
    C = cmyk_image[:, :, 0] / 255.0
    M = cmyk_image[:, :, 1] / 255.0
    Y = cmyk_image[:, :, 2] / 255.0
    K = cmyk_image[:, :, 3] / 255.0

    R = 255 * (1 - C) * (1 - K)
    G = 255 * (1 - M) * (1 - K)
    B = 255 * (1 - Y) * (1 - K)

    rgb_image = np.dstack((R, G, B)).astype(np.uint8)

    return rgb_image


def rgb2cmyk(
    img: cv2.typing.MatLike,
    rgb_scale: float = 255.0,
    cmyk_scale: float = 255.0,
) -> tuple[
    cv2.typing.MatLike,
    cv2.typing.MatLike,
    cv2.typing.MatLike,
    cv2.typing.MatLike,
]:
    R = img[:, :, 2].astype(np.float16) / rgb_scale
    G = img[:, :, 1].astype(np.float16) / rgb_scale
    B = img[:, :, 0].astype(np.float16) / rgb_scale

    C, M, Y = 1 - R, 1 - G, 1 - B
    K = np.minimum.reduce([C, M, Y])

    C = (C - K) * cmyk_scale
    M = (M - K) * cmyk_scale
    Y = (Y - K) * cmyk_scale
    K = K * cmyk_scale

    return C.astype(np.uint8), M.astype(np.uint8), Y.astype(np.uint8), K.astype(np.uint8)


# thresholding


def intermean(hist: cv2.typing.MatLike, t: int, start: int, end: int) -> int:
    prob = np.zeros_like(hist, dtype=np.float16)
    total = np.sum(hist[start:end])
    prob[start:end] = hist[start:end] / total

    w0 = np.sum(prob[start:t]) + 0.0000001
    w1 = (1 - w0) + +0.0000001
    # print('w1', w1)

    t0 = np.array(list(range(start, t)))
    t1 = np.array(list(range(t, end)))

    u0 = np.sum(t0 * prob[start:t]) / w0
    u1 = np.sum(t1 * prob[t:end]) / w1

    if u0 == 0.0:
        thr = u1
    elif u1 == 0.0:
        thr = u0
    else:
        thr = (u0 + u1) / 2

    return thr.astype(np.int16)  # type: ignore


def apply_threshold(img: cv2.typing.MatLike, thresh: int | None = None, inverse: bool = False) -> cv2.typing.MatLike:
    result = np.zeros_like(img, dtype=np.uint8)
    thresh = thresh or int(np.mean(img))  # type: ignore
    if inverse:
        result[img <= thresh] = 255
    else:
        result[img >= thresh] = 255
    return result


def histogram(img: cv2.typing.MatLike) -> cv2.typing.MatLike:
    row, col = img.shape
    hist = [0.0] * 256
    for i in range(row):
        for j in range(col):
            hist[img[i, j]] += 1
    return np.array(hist)


def show_histogram(h: cv2.typing.MatLike, opt: bool) -> None:
    plt.figure(figsize=(4, 2))
    plt.plot(h)
    plt.title('Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    if opt:
        plt.axis('on')
    else:
        plt.axis('off')
    plt.show()


def calculate_threshoding_by_intermean(
    img: cv2.typing.MatLike,
    *,
    tolerant: int = 1,
    times: int = 3,
) -> tuple[cv2.typing.MatLike, int]:
    hist = histogram(img)

    start, end = 0, 256
    final_thresh = 0

    for _ in range(times):
        t0 = int((start + end) * 0.5)
        t_list = [t0]

        while True:
            t1 = intermean(hist, t0, start, end)
            t_list.append(t1)
            if abs(t1 - t0) < tolerant:
                break
            t0 = t1

        final_thresh = t_list[-1]
        start = final_thresh + 1

    _, binary_img = cv2.threshold(img, final_thresh, 255, cv2.THRESH_BINARY)
    return binary_img, final_thresh


def otsu(hist: cv2.typing.MatLike, start: int, end: int) -> int:
    prob = np.zeros_like(hist, dtype='float16')
    total = np.sum(hist[start:end])
    prob[start:end] = hist[start:end] / total

    coef_max = -1
    thr = -1

    for t in range(start + 1, end - 1):
        w0 = np.sum(prob[start:t]) + 0.00000001
        w1 = np.sum(prob[t:end]) + 0.00000001

        i0 = np.array(list(range(start, t)))
        i1 = np.array(list(range(t, end)))

        u0 = np.sum(i0 * prob[start:t]) / w0
        u1 = np.sum(i1 * prob[t:end]) / w1

        coef = (w0 * w1) * np.power(u0 - u1, 2)
        if coef > coef_max:
            coef_max = coef
            thr = t

    return thr


def edge_operator_meth(img: cv2.typing.MatLike, k: int) -> cv2.typing.MatLike:
    f = img.copy().astype(np.float32)
    out = np.zeros_like(img, dtype=np.float32)
    mask_gx = np.array(
        [
            [-1, 0, 1],
            [-k, 0, k],
            [-1, 0, 1],
        ],
        dtype='float16',
    )
    mask_gy = np.array(
        [
            [-1, -k, -1],
            [0, 0, 0],
            [1, k, 1],
        ],
        dtype='float16',
    )
    sz, sz = mask_gx.shape
    bd = sz // 2
    (m, n) = f.shape
    for i in range(bd, m - bd):
        for j in range(bd, n - bd):
            gx, gy = 0.0, 0.0
            sub_f = f[i - bd : i + bd + 1, j - bd : j + bd + 1]
            # multiply คูณกัน ตำแหน่งที่ตรงกัน และ หาผลบวก
            gx = np.multiply(sub_f, mask_gx).sum()
            gy = np.multiply(sub_f, mask_gy).sum()
            out[i, j] = np.sqrt(gx**2 + gy**2)
    out[out > 255.0] = 255.0
    return out.astype(np.uint8)

def merge_quarters(
    img: cv2.typing.MatLike,
    sub11: cv2.typing.MatLike,
    sub12: cv2.typing.MatLike,
    sub21: cv2.typing.MatLike,
    sub22: cv2.typing.MatLike,
) -> cv2.typing.MatLike:
    out = np.zeros_like(img, dtype='uint8')
    h, w = img.shape
    wc, hc = w // 2, h // 2
    out[:hc, :wc] = sub11
    out[hc:, :wc] = sub12
    out[:hc, wc:] = sub21
    out[hc:, wc:] = sub22

    return out

def split_sub_image(img: cv2.typing.MatLike) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike]:
    _, w = img.shape
    w_cutoff = w // 2
    img_left = img[:, :w_cutoff]
    img_right = img[:, w_cutoff:]
    return img_left, img_right

def split_image_quarters(
    img: cv2.typing.MatLike,
) -> tuple[cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]:
    sub1, sub2 = split_sub_image(img)

    sub11, sub12 = split_sub_image(sub1.transpose())
    sub21, sub22 = split_sub_image(sub2.transpose())
    sub11, sub12 = sub11.transpose(), sub12.transpose()
    sub21, sub22 = sub21.transpose(), sub22.transpose()

    return sub11, sub12, sub21, sub22
