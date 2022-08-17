import cv2
import numpy as np

frameWidth = 720
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(5, 150)


colors = [[47, 194, 166, 172, 255, 255], [0, 135, 235, 86, 255, 255]]
RWColors = [[0, 0, 255], [255, 255, 255]]
points = []

def findColor(img, colors, RWColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    nPoints = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = getContour(mask)
        cv2.circle(imgContour, (x, y), 5, RWColors[count], cv2.FILLED)
        if x != 0 and y != 0:
            nPoints.append([x, y, count])
        count += 1
    return nPoints


def getContour(img):
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy =cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def draw(points, RWColors):
    for point in points:
        cv2.circle(imgContour, (point[0], point[1]), 10, RWColors[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgContour = img.copy()
    nPoints = findColor(img, colors, RWColors)
    if len(nPoints) != 0:
        for n in nPoints:
            points.append(n)
    if len(points) != 0:
        draw(points, RWColors)
    cv2.imshow("Original", cv2.flip(imgContour, 1))
    # cv2.imshow("HSV", imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break