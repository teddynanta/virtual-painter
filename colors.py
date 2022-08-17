import cv2
import numpy as np

cap = cv2.VideoCapture(0)
frameWidth = 480
frameHeight = 240
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(5, 150)

colors = [[47, 172, 194, 255, 166, 255], [0, 86, 135, 255, 235, 255]]

def e(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 47, 179, e)
cv2.createTrackbar("Hue Max", "Trackbars", 172, 179, e)
cv2.createTrackbar("Sat Min", "Trackbars", 194, 255, e)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, e)
cv2.createTrackbar("Value Min", "Trackbars", 166, 255, e)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, e)


while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hMin = cv2.getTrackbarPos("Hue Min", "Trackbars")
    hMax = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sMin = cv2.getTrackbarPos("Sat Min", "Trackbars")
    sMax = cv2.getTrackbarPos("Sat Max", "Trackbars")
    vMin = cv2.getTrackbarPos("Value Min", "Trackbars")
    vMax = cv2.getTrackbarPos("Value Max", "Trackbars")
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    print(hMin, hMax, sMin, sMax, vMin, vMax)
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("Mask", mask)
    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break