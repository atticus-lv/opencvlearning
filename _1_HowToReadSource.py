#-*- coding =utf-8 -*-
import cv2

def readimg():
    img = cv2.imread("res/lena.png")  #读取图片
    cv2.imshow("output image",img)    #显示图片
    cv2.waitKey(0)    #延长图片显示时间

def readvideo():
    video = cv2.VideoCapture('res/test_video.mp4')  #读取视频
    # 通过循环来延迟视频（每一帧）
    while 1:
        success,img = video.read()    # read读取视频
        cv2.imshow("video show",img)  # 显示图片
        if cv2.waitKey(1) & 0xFF == ord("q"): #ord函数：将字符转回ASCII对应数值
            break


def readcam():
    cam = cv2.VideoCapture(1) #数字代表读取相机， 0，1
    cam.set(3,640)  # 3代表宽度
    cam.set(4,480)  # 4代表高度
    cam.set(10,10)    # 10 代表亮度


    while 1:
        success,img = cam.read()    # read读取视频
        cv2.imshow("camera",img)  # 显示图片
        if cv2.waitKey(1) & 0xFF == ord("q"):  #ord函数：将字符转回ASCII对应数值
            break