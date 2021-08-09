# import cv2
# img = cv2.imread("C:/Users/lodha/Desktop/wp6557115.png")
#
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)


# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("C:/naruto/-animeawake- Naruto Shippuden Episode 344.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break


import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break