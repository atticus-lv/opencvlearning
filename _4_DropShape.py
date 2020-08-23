import cv2
import numpy as np

#
img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
#矩形上色（同裁切图片）
# img[200:300,100:300] = 255,0,0

#线：图片，开始点，结束点，颜色等
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),thickness=2)

# 可以使用 thickness = cv2,FULLED 填充正方形
cv2.rectangle(img=img,pt1=(0,0),pt2=(250,350),
              color=(0,0,255),thickness=2)

cv2.circle(img,(400,50),30,(255,255,0),3)

cv2.putText(img,"opencv",(300,300),cv2.FONT_HERSHEY_COMPLEX,1,
            (222,111,222),2)


cv2.imshow("img",img)

cv2.waitKey(0)