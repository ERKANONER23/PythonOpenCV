import cv2

resim=cv2.imread("NecipFazilKisakurek.jpg",0)

cv2.imshow("Ustad",resim)

dugme=cv2.waitKey(0)

if dugme==27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite("Adam Olmak.jpg",resim)
    cv2.destroyAllWindows()

