import cv2

class Capture:

    def videoCaptureFrame(self, port):
        capturer = cv2.VideoCapture(port)
        while True:
            ret, frame = capturer.read()
            cv2.imshow("Preview", frame)
            cv2.imwrite("images/temp/temp.jpg", frame)
            k = cv2.waitKey(1)
            if k == 27:
                break

    def captureImage(self, port):
        ImageCaptureObject = cv2.VideoCapture(port)
        result = True
        while(result):
            ret,frame = ImageCaptureObject.read()
            cv2.imwrite("images/temp/temp.jpg", frame)
            result = False
        ImageCaptureObject.release()
        cv2.destroyAllWindows()

    def getImage(self, imagePath):
        self.image = cv2.imread(imagePath)
        return self.image
    
    def getVideo(self,  port):
        self.cap = cv2.VideoCapture(port) #port will be in GUI to be mutable

        assert self.cap.isOpened() , "Could not open video device, make sure you've selected right port"

        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('U', 'Y', 'V', 'Y'))

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while(True):
            ret, frame = self.cap.read()

            cv2.imshow('preview',frame)
            k = cv2.waitKey(1)
            if (k == 27): 
                break
            elif k == ord("a"):
                cv2.imwrite("images/temp/temp.jpg", frame)
                break

    def getVideoAttributes(self):

        Brightness=self.cap.get(cv2.CAP_PROP_BRIGHTNESS)
        Contrast=self.cap.get(cv2.CAP_PROP_CONTRAST)
        Saturation=self.cap.get(cv2.CAP_PROP_SATURATION)
        Gain=self.cap.get(cv2.CAP_PROP_GAIN)
        Hue=self.cap.get(cv2.CAP_PROP_HUE)
        Exposure=self.cap.get(cv2.CAP_PROP_EXPOSURE)

        VideoAttributes = {"brightness": Brightness
                           ,"contrast": Contrast
                           ,"caturation": Saturation
                           ,"gain": Gain
                           ,"hue": Hue
                           ,"exposure": Exposure
                           }
        
        return VideoAttributes        