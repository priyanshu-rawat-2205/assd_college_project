import cv2

class ShotDetector:

    points = []

    def __init__(self, thAdaptive, wrappedImage, cleanTarget):

        self.image = wrappedImage
        self.shotTarget = cleanTarget
        contours, hierarchy = cv2.findContours(thAdaptive, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        font = cv2.FONT_HERSHEY_COMPLEX
        for c in contours:
            if cv2.contourArea(c) < 400 and cv2.contourArea(c) > 85 : #min and max area will be mutable in GUI
                # print(cv2.contourArea(c))
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(self.shotTarget, (x, y), (x + w, y + h), (0, 255,0), 2)
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255,0), 2)
                string = "(" + str(x) + ", " + str(y) + ")"
                center = (x,y)
                self.points.append(center)
            else:
                continue
    
    def returnShotImage(self):
        return self.image
    
    def returnShotTarget(self):
        return self.shotTarget

    def returnShotPoints(self):
        return self.points