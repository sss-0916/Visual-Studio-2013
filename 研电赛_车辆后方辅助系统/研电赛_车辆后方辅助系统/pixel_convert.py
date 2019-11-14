import cv2

img = cv2.imread('D:/img/img_190617/img_q/left_5.bmp')

cv2.imshow("img", img)
cv2.waitKey(200)

temp = cv2.resize(img, (640, 360))

cv2.imshow("temp", temp)
cv2.waitKey(2000)

cv2.imwrite("temp.bmp", temp)