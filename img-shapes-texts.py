import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

# Black Image
img = np.zeros((512, 512, 3), np.uint8) 
cv2.imshow("Black Image", img)

# Color Image
img[:] = 255, 0, 0
cv2.imshow("Blue Image", img)

# Create Lines (start, end, color, thickness)
cv2.line(img, (0,0), (300,300), (0,255,0), 3)
cv2.imshow("Draw Line", img)

# Create a Rectangle (start, end, color, thickness)
cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED)
cv2.imshow("Draw Rectangle", img)

# Create a Circle (radio, color, thickness)
cv2.circle(img, (400,50), 30, (255,255,0), 5)
cv2.imshow("Draw a Circle", img)

# Put Text in the Image (image, text, coords, font, color, tickness)
cv2.putText(img, "This is the Text", (300,100), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 1)
cv2.imshow("Put Text", img)

# Wait 5 secs. then close window
# cv2.waitKey(5000)

# Close window when key is pressed
cv2.waitKey(0)