import cv2
import numpy as np
from _stackImages import stackImages


#该方法无法resize ，并且通道数必须相同
# img_hor = np.hstack((img, img))
# img_ver = np.vstack((img,img))
#
# cv2.imshow("hori", img_hor)
# cv2.imshow("ver", img_ver)


img = cv2.imread("res/lena.png")

# imgstack = stackImages(0.5,([img,img,img],[img,img,img]))
#
# cv2.imshow("ver", imgstack)

cv2.waitKey(0)
