import cv2
import numpy as np
from utils import *

def process(img, gamma=None, edge=False, blur_size=None):
    result = img.copy()
    
    if gamma is not None:
        result = power_gamma(result, gamma)

    if edge:
        result = sobel_operator(result)

    if blur_size is not None:
        result = cv2.blur(result, blur_size).astype(np.uint8)

    return result

# อ่านรูป
img = cv2.imread("./images/frame_ivus.png", 0)
show_image_plt(img, gray=True, title='Original')

#Test
show_images_plt([img, img, img])

# 1.1 Power Gamma 0.5
gamma_05 = process(img, gamma=0.5)
show_images_plt(img, gamma_05, titles=['Original', 'Power gamma 0.5'])
muls1 = cv2.hconcat([img, gamma_05])
cv2.imwrite('./images/outs/assignment1/frame_ivus_ass1.png', muls1)

# 1.2 Power Gamma 3
gamma_3 = process(img, gamma=3)
show_images_plt(img, gamma_3, titles= ['Original', 'Power gamma 3'])

# 1.3 Sobel Edge Detection
edge_img = process(img, edge=True)
show_images_plt(img, edge_img, titles=['Original', 'Sobel Edge'])

# 1.3.2 เอารูป 1.3.1 มาทำ gamma แล้วก็ทำ AverageBlur แล้วทำ Edge อีกที
edge_img_gamma = process(edge_img, 0.5, edge=True, blur_size=(3,3))
show_image_plt(edge_img_gamma, gray=True, title='Final Edge')



#---------------------------------------------- End ----------------------------------------------
"""
# 1.3.2 เอารูป 1.3.1 มาทำ gamma แล้วก็ทำ AverageBlur แล้วทำ Edge อีกที
edge_img_gamma = power_gamma(edge_img, 0.5)

#Average blur
edge_img_gamma_meam = cv2.blur(edge_img_gamma, (3,3)).astype(np.uint8)
show_image_plt(edge_img_gamma_meam, gray=True, title='Average blur')

#Average blur Edge
edge2_img = sobel_operator(edge_img_gamma_meam)
show_image_plt(edge2_img, gray=True)

show_images_plt(edge_img_gamma, edge_img_gamma_meam, edge2_img, titles=['Sobel Edge gamma', 'Average blur', 'Final Sobel Edge'])
"""