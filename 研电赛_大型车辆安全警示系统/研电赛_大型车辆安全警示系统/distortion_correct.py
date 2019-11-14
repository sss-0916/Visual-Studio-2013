import camera_configs
import cv2

#img = cv2.imread("D:\img\img_q\Camera_Roll\l5.jpg")
img = cv2.imread("D:\img\img_q\left_0.bmp")
#img1 = cv2.imread("./BG.jpg")

undistorted_img = cv2.remap(
    img, camera_configs.up_map1, camera_configs.up_map2, interpolation = cv2.INTER_LINEAR,
    borderMode = cv2.BORDER_CONSTANT
)    

cv2.namedWindow("img", 0)
cv2.resizeWindow("img", 800, 600)
#cv2.namedWindow("img1", 0)
#cv2.resizeWindow("img1", 640, 480)

cv2.imwrite("result.jpg", undistorted_img)

#while True:
#    cv2.imshow("img", undistorted_img)
#    #cv2.imshow("img1", img1)
#    cv2.imwrite("result.jpg", undistorted_img)
#    cv2.waitKey(1)