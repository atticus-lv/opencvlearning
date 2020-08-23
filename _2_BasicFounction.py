#-*- coding =utf-8 -*-
import cv2
import numpy as np
from _stackImages import stackImages

img = cv2.imread("res/lena.png")
kl = np.ones((5,5),np.uint8) #增厚强度

#rgb转黑白 注意为 BGR
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray image",img_grey)


# 高斯模糊
img_blur = cv2.GaussianBlur(img_grey,(5,5),0)
# cv2.imshow("blur image",img_blur)


#边缘检测
img_canny = cv2.Canny(img,100,100)
img_canny1 = cv2.Canny(img,100,200)
img_canny2 = cv2.Canny(img,150,200)
# cv2.imshow("canny image",img_canny)
# cv2.imshow("canny1 image",img_canny1)
# cv2.imshow("canny2 image",img_canny2)

# 扩张，增厚边缘检测后的图片
img_dialation = cv2.dilate(img_canny,kl,iterations=1)

# 侵蚀，
img_eroded = cv2.erode(img_dialation,kl,iterations=1)

# cv2.imshow("dialation image",img_dialation)
# cv2.imshow("eroderd image",img_eroded)


stackimg = stackImages(0.5,([img,img_grey,img_blur],
                            [img_canny,img_canny1,img_dialation]))
cv2.imshow("image",stackimg)

cv2.waitKey(0)