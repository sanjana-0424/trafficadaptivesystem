import cv2

cap = cv2.VideoCapture("traffic.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    mask = fgbg.apply(frame)

    cv2.imshow("Original Video", frame)

    cv2.imshow("Vehicle Detection", mask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()