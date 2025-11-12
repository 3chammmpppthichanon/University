
import cv2
import matplotlib.pyplot as plt
import numpy as np
from utils import *

img = cv2.imread("./images/images/frame_ivus.png", cv2.IMREAD_GRAYSCALE)
gamma = 0.5

print(img.shape)
print(img.dtype)


img_norm = img.astype(np.float16)
img_norm = img_norm / np.amax(img_norm)
print(img_norm)

gamma_img = (img_norm*gamma) * 255.0
gamma_img = gamma_img.astype(np.uint8)
print(gamma_img)

muls_img = cv2.hconcat([img, gamma_img])
cv2.imwrite('./outs/img2.png', muls_img.astype(np.uint8))


plt_image(img, gray=True)


img_norm = normalize(img)
plt_image(img_norm, gray=True)


img_gamma = power_gamma(img_norm, 0.5)
plt_image(img_gamma, gray=True)