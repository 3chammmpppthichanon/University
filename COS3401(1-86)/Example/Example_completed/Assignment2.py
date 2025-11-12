import numpy as np
import cv2
import matplotlib.pyplot as plt
from utils import *

img = cv2.imread('./images/images/dark_image.png', 0)

img2 = cv2.imread("./images/images/bright_image.png", 0)

def cv2_show_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plt_show_image(img):
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.show()

def edge_operator_meth(img, k):
    f = img.copy().astype(np.float16)
    out = np.zeros_like(img, dtype = 'float16')
    mask_gx = np.array([[-1, 0, 1], [-k, 0, k], [-1, 0, 1]] , dtype = 'float16') 
    mask_gy = np.array([[-1, -k, -1], [0, 0, 0], [1, k, 1]] , dtype = 'float16') 
 
    sz, sz = mask_gx.shape
    bd = sz // 2
    (m,n) = f.shape
    for i in range(bd,m-bd):
        for j in range(bd,n-bd):
            gx, gy = 0., 0.
            sub_f = f[i - bd : i + bd + 1, j - bd : j + bd + 1]
            gx = np.multiply(sub_f, mask_gx).sum() 
            gy = np.multiply(sub_f, mask_gy).sum()    
            out[i,j] = np.sqrt(gx**2 + gy**2)
    out[out>255.0] = 255.0
    return out.astype(np.uint8)

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


