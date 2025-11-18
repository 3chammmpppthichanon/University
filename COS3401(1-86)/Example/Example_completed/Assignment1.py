import cv2
import matplotlib.pyplot as plt
import numpy as np
from utils import *

img = cv2.imread("./images/frame_ivus.png", cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img.dtype)

gamma_img = power_gamma(img, 0.5)
print(gamma_img)

muls_img = cv2.hconcat([img, gamma_img])
cv2.imwrite('./outs/img2.png', muls_img.astype(np.uint8))