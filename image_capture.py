import cv2
import numpy as np

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cv2.namedWindow("test_left")
cv2.namedWindow("test_right")

img_counter = 0

while True:
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    cv2.imshow("test_left", frame1)
    cv2.imshow("test_right", frame2)
    if not ret1:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img1_name = "left_image2.png"
        cv2.imwrite(img1_name, cv2.resize(frame1, (300,300)))
        img2_name = "right_image2.png"
        cv2.imwrite(img2_name, cv2.resize(frame2, (300, 300)))
        print("Image captured")

cam1.release()
cam2.release()

cv2.destroyAllWindows()