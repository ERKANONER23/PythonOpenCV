import cv2
import numpy as np

cerceve= np.zeros((512,512,3),np.uint8)

cv2.line(cerceve,(50,50),(400,300),(255,255,255),50)

cv2.imshow("cerceve",cerceve)