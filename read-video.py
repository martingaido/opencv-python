import cv2

print("OpenCV Version:", cv2.__version__)

cap = cv2.VideoCapture("videos/IMG_4442.MOV")

while True:
    success, img = cap.read()
    cv2.imshow("Window Name Here", img)

    # Press Q to exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
