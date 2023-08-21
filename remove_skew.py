import numpy as np
import cv2

webCamfeed = True
image_path = "images/capture1.jpeg"
cap = cv2.VideoCapture(2)
cap.set(10,160)
# cap.set(cv2.CAP_PROP_EXPOSURE, 100)

while(True):
     # Capture each frame of webcam video
     ret,frame = cap.read()
     cv2.imshow("My cam video", frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break
