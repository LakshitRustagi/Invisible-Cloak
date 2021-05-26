import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
back = cv2.imread('background.jpg')

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    # Converting from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow('hsv', hsv)
    # Value of green colour in BGR format
    green = np.uint8([[[0, 255, 0]]])
    # Converting from BGR to HSV
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    # print(hsv_green)
    # Our frame, the HSV image, is thresholded among upper and lower pixel ranges to get only green colors
    lower = np.array([40, 40, 40])
    upper = np.array([80, 255, 255])
    # Creating a mask such that only green coloured items are visible
    mask = cv2.inRange(hsv, lower, upper)
    # cv2.imshow('mask',mask)
    # Using Morphology techniques for better image
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Replacing the cloak(green-coloured) with the background image
    part1 = cv2.bitwise_and(back, back, mask=mask)
    # cv2.imshow('mask', mask)
    # Updating the previous mask such that all except green coloured are visible
    mask = cv2.bitwise_not(mask)
    # Replacing the non-green coloured area with our original frame
    part2 = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('image', part1+part2)

    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
