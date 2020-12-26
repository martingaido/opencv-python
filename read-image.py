import cv2

print("OpenCV Version:", cv2.__version__)

img = cv2.imread("images/color-paint.jpg")
cv2.imshow("Window Name Here", img)

# Wait 5 secs. then close window
cv2.waitKey(5000)

# Close window when key is pressed
# cv2.waitKey(0)