import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()

# show the images
while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (0, 255, 0), cutThreshold=0.8)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    cv2.imshow("Image", imgStacked)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

