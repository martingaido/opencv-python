import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

img = cv2.imread("images/color-paint.jpg")

# Get the size of the image
print(img.shape)

# Define Corners
width, height = 250, 350
pts1 = np.float32([[111,219],[287,188],[152,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transform", imgOutput)

# Wait 5 secs. then close window
# cv2.waitKey(5000)

# Close window when key is pressed
cv2.waitKey(0)