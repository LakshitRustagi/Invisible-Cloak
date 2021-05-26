import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    cv2.imshow('background', frame)
    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        cv2.imwrite('background.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
