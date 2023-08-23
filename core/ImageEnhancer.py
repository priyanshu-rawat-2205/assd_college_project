import cv2

class ImageEnhancer:

    def __init__(self, transformedImage):
        gray = cv2.cvtColor(transformedImage, cv2.COLOR_BGR2GRAY)

        #all these parameters passed in function will be mutable in GUI
        blurred = cv2.GaussianBlur(gray, (5,5), 1)
        thadaptive = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        self.image = thadaptive

    def returnEnhanced(self):
        return self.image