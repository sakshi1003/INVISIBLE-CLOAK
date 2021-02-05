# Import Libraries

import numpy as np
import cv2

import time

cap=cv2.VideoCapture(0)

time.sleep(2)

background=0

for i in range(60):
    ret,baclgroud=cap.read()
    while(cap.isOpened()):
        ret,img=cap.read()
        if not ret:
            break
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        #HSV values
        lower_red=np.array([0,120,70])
        upper_red=np.array([10,255,265])
        mask1=cv2.inRange(hsv,lower_red,upper_red)

        lower_red=np.array([170,120,70])
        upper_red=np.array([180,255,255])
        mask2=cv2.inRange(hsv,lower_red,upper_red)
        mask=mask1+mask2#ORI or X
        mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,
        np.ones((3,3) ,np.uint8), iterations=2)
        mask2=cv2.morphologyEx(mask2,cv2.MORPH_DILATE,
        np.ones((3,3) ,np.uint8) ,iterations=1)
        mask2 =cv2.bitwise_not(mask1)
        res1=cv2.bitwise_and(background ,background, mask=mask1)
        res2=cv2.bitwise_and(img, img, mask=mask2)
        final_output=cv2.addweighted(res1,1,res2,1,0)
        cv2.imshow('Eureka!!',final_output)
        k=cv2.waitkey(10)
        if k==27:
            breakp
        cap.release()
        cv2.destroyAllWindows()


    