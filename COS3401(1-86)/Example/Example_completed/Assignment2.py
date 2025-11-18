import numpy as np
import cv2
import matplotlib.pyplot as plt
from utils import *

def cv2_show_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plt_show_image(img):
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.show()

img = cv2.imread('./images/frame_ivus.png', 0)
img2 = cv2.imread('./images/bright_image.png', 0)

# 2.1
img_edge_prewitt = edge_operator_meth(img, 1)
plt_show_image(img_edge_prewitt)

img_edge_sobel = edge_operator_meth(img, 2)
plt_show_image(img_edge_sobel)

muls = cv2.hconcat([img_edge_prewitt, img_edge_sobel])
plt_show_image(muls)

# 2.2
plt_show_image(img2)

img2_gamma = power_gamma(img2, 5)
plt_show_image(img2_gamma)

img2_edge_prewitt = edge_operator_meth(img2_gamma,1)
plt_show_image(img2_edge_prewitt)

img2_edge_sobel = edge_operator_meth(img2_gamma, 2)
plt_show_image(img2_edge_sobel)