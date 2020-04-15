import cv2
import numpy as np

def bos(a):
    pass

pencere=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("renkler")

cv2.createTrackbar("Red","renkler",0,255,bos)
cv2.createTrackbar("Green","renkler",0,255,bos)
cv2.createTrackbar("Blue","renkler",0,255,bos)
cv2.createTrackbar("OnOff","renkler",0,1,bos)

while(True):
    cv2.imshow("renkler",pencere)
    klavye=cv2.waitKey(1) & 0xFF
    if klavye==27:
        break;
    kirmizi=cv2.getTrackbarPos("Red","renkler")
    yesil=cv2.getTrackbarPos("Green","renkler")
    mavi=cv2.getTrackbarPos("Blue","renkler")
    akfif=cv2.getTrackbarPos("OnOff","renkler")
    
    if akfif==0:
        pencere[:]=0
    else:
        pencere[:]=[kirmizi,yesil,mavi]
    