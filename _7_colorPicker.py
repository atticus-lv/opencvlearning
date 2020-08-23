import cv2
import numpy as np
from _stackImages import stackImages

path = "res/lambo.PNG"

def update(a):
    pass

#创建新窗口
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",500,250)
#定义状态栏参数
cv2.createTrackbar("Hue Min","TrackBars",3,179,update)
cv2.createTrackbar("Hue Max","TrackBars",19,179,update)
cv2.createTrackbar("Sat Min","TrackBars",71,255,update)
cv2.createTrackbar("Sat Max","TrackBars",255,255,update)
cv2.createTrackbar("Val Min","TrackBars",94,255,update)
cv2.createTrackbar("Val Max","TrackBars",255,255,update)





while 1:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #cv2.getTrackbarPos() 获取状态栏
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    low = np.array([h_min,s_min,v_min])
    high = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,low,high)

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)

    imagestacks = stackImages(0.5,([img,imgHSV],[mask,mask]))
    cv2.imshow("show", imagestacks)
    cv2.waitKey(1)