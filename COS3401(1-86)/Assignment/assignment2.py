import numpy as np
import cv2
from utils import *

def process(img, gamma=None, edge=False, equalize=False):
    result = img.copy()
    
    if gamma is not None:
        result = power_gamma(result, gamma)

    if edge:
        result = sobel_operator(result)

    if equalize:
        result = cv2.equalizeHist(img)

    return result

# อ่านรูป
img = cv2.imread('./images/dark_image.png', 0)
show_image_plt(img, gray=True, title='Original')

# 2.1 เอารูปดั้งเดิมไปทำ Edge Detection
img_sobel = process(img, edge=True)
show_images_plt(img, img_sobel, titles=['Original images', 'Sobel Edge'])

#2.2 เอารูปดั้งเดิมมาทำ Equalize แล้ว ทำ Edge
img_equalize_sobel = process(img, equalize=True, edge=True)
show_image_plt(img_equalize_sobel, gray=True)
show_images_plt(img, img_equalize_sobel, titles=['Original', 'Equalization Sobel Edge'])

#2.3 เอารูปดั้งเดิมมาทำ Powergamma ก่อนแล้วทำ Equalize แล้ว ทำ Edge
img2 = cv2.imread('./images/bright_image.png', 0)

show_image_plt(img2, gray=True, title='Original')

gamma_img2 = power_gamma(img2, 5)

show_image_plt(gamma_img2, gray=True, title='Gamma 5')

equali_img2 = cv2.equalizeHist(gamma_img2)

show_image_plt(equali_img2, gray=True, title='Equalization')

sobel_img2 = sobel_operator(equali_img2)

show_image_plt(sobel_img2, gray=True, title='Sobel Edge')

# 2.4 แสดงผลเอาทุกข้อก่อนหน้ามาเทียบกัน
show_images_plt(img2, gamma_img2, equali_img2, sobel_img2, titles=['Original image 2', 'Gamma 5', 'Equalization', 'Sobel'])

muls = cv2.hconcat([img2, gamma_img2, equali_img2, sobel_img2])

cv2.imwrite('./images/outs/assignment2/2final.png',muls )