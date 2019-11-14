import numpy as np
import cv2

K = np.array([[414.22607, 0., 381.76500],
             [0., 424.64700, 276.82032],
             [0., 0., 1.]])

D = np.array([[0.23918, -0.23275, -0.01125, 0.01405]])

img = cv2.imread("D:\img\img_q\Camera_Roll\l5.jpg")

DIM = (img.shape[:2])[::-1]
#print(DIM)

#img = cv2.resize(img, DIM)
map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM,cv2.CV_16SC2)
undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)    
#undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR)    
#cv2.imwrite("unfisheyeImage.png", undistorted_img)

cv2.namedWindow("img", 0)
cv2.resizeWindow("img", 640, 480)

#print(img.shape[:2])
#print((img.shape[:2])[::-1])

#cv2.imwrite("img16.jpg", undistorted_img)

while True:
    cv2.imshow("img", undistorted_img)
    cv2.waitKey(1)