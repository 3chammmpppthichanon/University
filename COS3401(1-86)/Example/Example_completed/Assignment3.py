
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import *

def cv2_show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_gray = cv2.imread('.images/document1.png', 0)

cv2.imshow("Image Gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,w = img_gray.shape
print(f"Height: {h}, Width: {w}")

mid_y = h // 2
mid_x = w // 2
print(f"Midpoint Y: {mid_y}, Midpoint X: {mid_x}")

q_tl = img_gray[0:mid_y, 0:mid_x]
q_tr = img_gray[0:mid_y, mid_x:w]
q_bl = img_gray[mid_y:h, 0:mid_x]
q_br = img_gray[mid_y:h, mid_x:w]
cv2_show_image("Top left quadrant", q_tr)

_, q_tl_final = cv2.threshold(q_tl, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2_show_image("Top left quadrant after Otsu's thresholding", q_tl_final)

# บนขวา
_, q_tr_final = cv2.threshold(q_tr, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2_show_image("Top right quadrant after Otsu's thresholding", q_tr_final)

# ล่างซ้าย
bl_cal, t = calculate_threshoding_by_intermean(q_bl)

q_bl_final = apply_threshold(q_bl, t, inverse=True)
cv2_show_image("Bottom left quadrant", q_bl_final)

#ขวาล่าง
cv2_show_image("Bottom left quadrant", q_br)
q_br_median = cv2.medianBlur(q_br, 3)

q_br_mean = int(np.mean(q_br_median))

q_br_final = apply_threshold(q_br_median, q_br_mean)
cv2_show_image("Bottom right quadrant", q_br_final)

all_img = merge_quarters(img_gray, q_tl_final, q_tr_final, q_bl_final, q_br_final)
cv2.imwrite("./outs/output_document1.png", all_img)