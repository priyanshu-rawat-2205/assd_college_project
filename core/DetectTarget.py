import cv2
import core.ImageUtility as iu

class DetectTarget:

    mouseX = 0
    mouseY = 0
    points = []

    def draw_circle(self,event,x,y,flags,param):
        global mouseX,mouseY
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(self.image,(x,y),5,(255,0,0),-1)
            self.mouseX, self.mouseY = x,y

    def __init__(self, image):
        # self.image = self.image_resize(image, 512, 512)
        file = open("core/temp/points.txt", "w")
        self.image = iu.ImageUtility.image_resize(image, 512, 512)
        pressedkey=cv2.waitKey(0)
        cv2.imshow('preview', self.image)
        if pressedkey==27:
            cv2.destroyAllWindows()
        cv2.namedWindow('image')
        cv2.setMouseCallback('preview',self.draw_circle)
        while(1):
            cv2.imshow('image',self.image)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
            elif k == ord('a'):
                file.write(str(self.mouseX) + "\n")
                file.write(str(self.mouseY) + "\n")
                print(self.mouseX, self.mouseY)
                # self.points.append([self.mouseX, self.mouseY])
        file.close()

    def returnPoints(self):
        count = 0
        lines = []
        with open('core/temp/points.txt', 'r') as file:
            while line := file.readline():
                if not line:
                    continue
                if count == 2:
                    self.points.append(lines)
                    count = 0
                    lines = []
                lines.append(int(line.strip()))
                count += 1
            self.points.append(lines)  
        return self.points
    
    def returnResized(self):
        return self.resized