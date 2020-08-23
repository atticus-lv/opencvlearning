#-*- coding =utf-8 -*-

import cv2

img = cv2.imread("res/lambo.PNG")

# open cv x从左到右为宽度 y从上到下为高度，
print(img.shape) # print 先 y 后x

# resize
img_resize = cv2.resize(img,(300,200))  #opencv中  先 x 后 y
print(img_resize.shape)

#裁剪
img_crop = img[0:200,200:500] # 先 y 后x

cv2.imshow("image",img)
# cv2.imshow("resize",img_resize)
cv2.imshow("crop",img_crop)

cv2.waitKey(0)