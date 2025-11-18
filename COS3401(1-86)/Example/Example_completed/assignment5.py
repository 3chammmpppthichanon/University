
import cv2
import numpy as np
from utils import *

img = cv2.imread('./images/shade.png', cv2.IMREAD_COLOR_RGB)
plt_image(img)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

img_hsv = hsv.astype(np.float32)
img_hsv[:,:,1] *= 0.5
img_hsv = img_hsv.astype(np.uint8)

result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
plt_image(result, gray=True)

result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
cv2.imwrite('./outs/assignment5.png', result_bgr.astype(np.uint8))