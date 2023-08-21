import cv2

videoCaptureObject = cv2.VideoCapture(2)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewP6.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()