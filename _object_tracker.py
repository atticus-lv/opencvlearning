import cv2
import time

#set camera / tracker
cam = cv2.VideoCapture(1)
cam.set(10,5)

tracker = cv2.TrackerMOSSE_create() #600fps
tracker = cv2.TrackerCSRT_create() #40fps

def main():
    img,bbox = pickimg(cam,tracker)
    track(cam,tracker,img,bbox)

    cv2.destroyAllWindows()
    cam.release()

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),1)
    pass


def pickimg(cam,tracker):
    while 1:
        success, img = cam.read()
        cv2.putText(img, "Mode:Init", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Track", img)
        cv2.putText(img, "Mode:Select", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if cv2.waitKey(1) & 0xff == ord("s"):
            bbox = cv2.selectROI("Track", img, False)
            tracker.init(img, bbox)
            return img,bbox


def track(cam,tracker,ori_img,ori_bbox):
    while 1:
        #记录fps
        timer = cv2.getTickCount()
        ret, img = cam.read()

        success,bbox = tracker.update(img)

        if success:
            drawBox(img,bbox)
            cv2.putText(img, "Mode:Track", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv2.putText(img,"Mode:Lost",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        cv2.putText(img,"FPS:"+ str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

        cv2.imshow("Track",img)

        if cv2.waitKey(1) & 0xff == ord("q"):
            break


if __name__ == '__main__':
    main()


