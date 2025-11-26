import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_image_cv2(img, title = ''):
    cv2.imshow(img, title)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_image_plt(img, title = '', gray = False):
    plt.axis('off')
    plt.imshow(img, cmap='gray' if gray else None)

    if title:
        plt.title(title)

    plt.show()

def show_images_plt(img1, img2, img3, titles=[]):

    fig = plt.figure()

    fig.add_subplot(131)
    plt.plot(img1)
    plt.title(titles[0])
    plt.axis('off')


    fig.add_subplot(132)
    plt.plot(img2)
    plt.title(titles[1])
    plt.axis('off')

    fig.add_subplot(133)
    plt.plot(img3)
    plt.title(titles[2])
    plt.axis('off')

    plt.show()

def power_gamma(img, gamma, c = 255.0):
    # ข้ันตอนการ Norm
    img_norm = img.astype(np.float16) / 255.0

    # การทำ power gamma และแปลงค่ากลับ
    gamma_img = (img_norm ** gamma) * c
    gamma_img = gamma_img.astype(np.uint8)

    return gamma_img


# หาขอบภาพ
def prewitt_operator_meth(img):
    mask_gx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype='float')
    mask_gy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype='float')
    gx = cv2.filter2D(img, -1, mask_gx)
    gy = cv2.filter2D(img, -1,  mask_gy)    
    out = np.sqrt(gx**2 + gy**2)
    return out.astype(np.uint8)

def sobel_operator(img):
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  
    out = np.sqrt(gx**2 + gy**2)
    return out.astype(np.uint8)

def reduce_saturation(img_hsv: cv2.typing.MatLike, percent: float) -> cv2.typing.MatLike:
    img_hsv = img_hsv.astype(np.float32)
    # (h: 0, s: 1, v: 2)
    img_hsv[:, :, 1] *= percent  # type: ignore
    return img_hsv.astype(np.uint8)


# color space
def rgb_to_cmyk(image):
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
    
    CMYK_image = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    
    return CMYK_image

def cmyk_to_rgb(cmyk_image):
    C = cmyk_image[:, :, 0] / 255.0
    M = cmyk_image[:, :, 1] / 255.0
    Y = cmyk_image[:, :, 2] / 255.0
    K = cmyk_image[:, :, 3] / 255.0

    R = 255 * (1 - C) * (1 - K)
    G = 255 * (1 - M) * (1 - K)
    B = 255 * (1 - Y) * (1 - K)

    rgb_image = np.dstack((R, G, B)).astype(np.uint8)

    return rgb_image

def intermean(hist, t):
    prob = hist/np.sum(hist)
    
    w0 = np.sum(prob[:t]) + 0.00000001
    w1 = np.sum(prob[t:]) + 0.00000001
    
    u0 = np.sum(np.array([i for i in range(t)])*prob[:t])/w0
    u1 = np.sum(np.array([i for i in range(t,256)])*prob[t:])/w1
    if (u0 == 0.0):
        thr = u1
    elif (u1 == 0.0):
        thr = u0
    else:
        thr = (u0 +u1) / 2

    return thr.astype('int16')


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