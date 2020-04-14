import cv2

izle=cv2.VideoCapture("Trees.mp4")
kodlama=cv2.VideoWriter_fourcc(*'XVID')
kaydet=cv2.VideoWriter("Agaclar.mp4",kodlama,30,(600,300))

while(True):
    okuma,kare=izle.read()
    if okuma==False:
        break
    else:
        cv2.imshow("Agaclar",kare)
        kaydet.write(kare)
    if cv2.waitKey(1) & 0xFF== ord("w"):
        break

kaydet.release()
izle.release()
cv2.destroyAllWindows()
