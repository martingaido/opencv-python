import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

img = cv2.imread("images/color-paint.jpg")

# Get the size of the image
print(img.shape)

# Resize Image
imgResized = cv2.resize(img, (300, 200))
cv2.imshow("Resized Image", imgResized)

# Crop Image
imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped Image", imgCropped)

# Wait 5 secs. then close window
# cv2.waitKey(5000)

# Close window when key is pressed
cv2.waitKey(0)