import cv2
import numpy as np
from utils import *

img = cv2.imread('./images/shade.png', cv2.IMREAD_COLOR_RGB)
plt_image(img)

#  CMYK
cmyk = rgb_to_cmyk(img)

c = cmyk[:, :, 0]
plt_image(c, gray=True)

binary_mask = np.zeros_like(c, dtype="uint8")

binary_mask[c >= 180] = 255
plt_image(binary_mask, gray=True)

binary_mask_median = cv2.medianBlur(binary_mask, 5)
plt_image(binary_mask_median, gray=True)

#HSV
plt_image(img)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

h, s, v = cv2.split(hsv)

h_double = h.astype(np.uint16) * 2

mask_h = ((h_double >= 0) & (h_double <= 150)) | ((h_double >= 330) & (h_double <= 360))
mask_s = (s >= 120) & (s <= 255)
mask_v = (v >= 70) & (v <= 255)

mask_bool = mask_h & mask_s & mask_v
mask_hsv = (mask_bool.astype(np.uint8)) * 255
plt_image(mask_hsv, gray=True)

mask_hsv_median_blur = cv2.medianBlur(mask_hsv, 5)
plt_image(mask_hsv_median_blur, gray=True)

result = cv2.hconcat([binary_mask_median, mask_hsv_median_blur])
plt_image(result, gray=True, title="CMYK vs HSV Masking")