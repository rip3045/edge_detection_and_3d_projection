import cv2
import numpy as np

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    cv2.imshow('left camera', cv2.resize(gray1, (300,300)))
    cv2.imshow('right camera', cv2.resize(gray2, (300, 300)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()