import cv2
import numpy as np


def empty(a):
    pass


path = 'C:/Users/lodha/Desktop/lena.png'

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("thresh1", "TrackBars", 0, 179, empty)
cv2.createTrackbar("thresh2", "TrackBars", 0, 179, empty)



while True:
    img = cv2.imread(path)
    t1 = cv2.getTrackbarPos("thresh1", "TrackBars")
    t2 = cv2.getTrackbarPos("thresh2", "TrackBars")
    edges = cv2.Canny(img, t1, t2)
    cv2.imshow("IMAGE",img)
    cv2.imshow("CANNY",edges)
    cv2.waitKey(1)