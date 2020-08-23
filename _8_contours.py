import cv2
import numpy as np
from _stackImages import stackImages

path = "res/shapes.png"

def update(x):
    pass

# 创建选择窗口
cv2.namedWindow("SelectShapeBar")
cv2.resizeWindow("SelectShapeBar",500,50)
cv2.createTrackbar("Shape Corners","SelectShapeBar",3,8,update)


img = cv2.imread(path)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey,(7,7),1)
img_canny = cv2.Canny(img_blur,50,50)

img_blank = np.zeros_like(img)
img_contour = img.copy()

def getContours(img,select_cors):
    #寻找外部结构
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area>500:
            # 绘制所有轮廓
            # cv2.drawContours(img_contour,cnt,-1,(255,0,0),3)
            # 获取轮廓长度
            peri = cv2.arcLength(cnt,True)
            # 获取每个点的位置
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #
            if len(approx) == select_cors :

                # 获取碰撞框
                x,y,w,h = cv2.boundingRect(approx)
                # 绘制正方形
                cv2.rectangle(img_contour,(x,y),(x+w,y+h),(255,0,0))


while 1:

    select_cors = cv2.getTrackbarPos("Shape Corners", "SelectShapeBar")
    getContours(img_canny,select_cors)

    showimages = stackImages(0.6,([img,img_grey,img_blur],[img_canny,img_contour,img_blank]))
    cv2.imshow("result",showimages)
    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break