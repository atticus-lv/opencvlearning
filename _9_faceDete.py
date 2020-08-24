import cv2

#定义人脸识别模型
face_cascade = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")

# img = cv2.imread("res/FACE.jpg")

def readcam():
    cam = cv2.VideoCapture(1) #数字代表读取相机， 0，1
    cam.set(3,640)  # 3代表宽度
    cam.set(4,480)  # 4代表高度
    cam.set(10,10)    # 10 代表亮度

    color = (255, 255, 255)

    while 1:
        success,img = cam.read()    # read读取视频
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #获取点
        faces = face_cascade.detectMultiScale(img_grey, 2.2, 7)

        # 绘制碰撞盒
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 4)
            cv2.putText(img, "FACE", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 1)


        cv2.imshow("camera",img)  # 显示图片
        if cv2.waitKey(1) & 0xFF == ord("q"):  #ord函数：将字符转回ASCII对应数值
            break

readcam()