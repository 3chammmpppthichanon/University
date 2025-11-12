import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/images/frame_ivus.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
