import cv2

# Print OpenCV Version
print("OpenCV Version:", cv2.__version__)

# Use default webcam
cap = cv2.VideoCapture(0)

# Print Default Webcam Width & Height
print("Cam Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Cam Heigth:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Brightness:", cv2.CAP_PROP_BRIGHTNESS)

# Define parameters
# More: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Window Name Here", img)

    # Press Q to exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
