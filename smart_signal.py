import cv2

cap = cv2.VideoCapture("traffic.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()


def get_signal_time(vehicle_count):

    if vehicle_count > 20:
        return 15

    elif vehicle_count > 10:
        return 10

    else:
        return 5


while True:

    ret, frame = cap.read()

    if not ret:
        break

    mask = fgbg.apply(frame)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    vehicle_count = 0

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:

            vehicle_count += 1

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )


    green_time = get_signal_time(vehicle_count)


    cv2.putText(
        frame,
        f"Vehicles: {vehicle_count}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Green Time: {green_time} sec",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Smart Traffic Signal", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()