import cv2

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)
camera3 = cv2.VideoCapture(2)

camera1.set(3, 640)
camera1.set(4, 360)
camera2.set(3, 640)
camera2.set(4, 360)
camera3.set(3, 800)
camera3.set(4, 600)

while True:
    ret1, frame1 = camera1.read()
    ret2, frame1 = camera1.read()
    ret3, frame1 = camera1.read()

    cv2.imshow("img1", frame1)
    cv2.imshow("img2", frame2)
    cv2.imshow("img3", frame3)

    cv2.waitKey(1)