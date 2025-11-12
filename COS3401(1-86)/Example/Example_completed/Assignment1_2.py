import cv2
from utils import *

img = cv2.imread("./images/images/frame_ivus.png", cv2.IMREAD_GRAYSCALE)
print(img)

print(img.shape)

img_norm = normalize(img)
print(img_norm)
print(img_norm.shape)

img_gamma = power_gamma(img_norm, gamma=1.5)

plt_image(img_gamma, gray=True)

muls_img = cv2.hconcat([img, img_gamma])
plt_image(muls_img, gray=True)

cv2.imwrite("./outs/1_2.png", img_gamma)