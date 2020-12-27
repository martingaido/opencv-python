import cv2
import numpy as np

img = cv2.imread('images/color-paint.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal Stack", imgHor)
cv2.imshow("Vertical Stack", imgVer)

cv2.waitKey(0)