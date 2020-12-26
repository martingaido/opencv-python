import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

img = cv2.imread("images/color-paint.jpg")
kernel = np.ones((5,5), np.uint8)

# Convert Image to Grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)

# Convert Image to Blur
imgBlur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Blur Image", imgBlur)

# Canny Edge Detector
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny Edge Detector", imgCanny)

# Image Dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Image Dialation", imgDialation)

# Image Erosion
imgErode = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Image Erosion", imgErode)

# Wait 5 secs. then close window
# cv2.waitKey(5000)

# Close window when key is pressed
cv2.waitKey(0)