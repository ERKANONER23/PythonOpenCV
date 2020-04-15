import cv2
import numpy as np

cerceve= np.zeros((512,512,3),np.uint8)

cv2.circle(cerceve,(256,256),(128),(255,255,255),50)

cv2.imshow("cerceve",cerceve)