import cv2
import numpy as np

mouseX = 0
mouseY = 0

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized

img=cv2.imread('images/plain_target.jpeg')
img = image_resize(img, 512, 512)
cv2.imshow('Test', img)

pressedkey=cv2.waitKey(0)

# Wait for ESC key to exit
if pressedkey==27:
    cv2.destroyAllWindows()

# img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('Test',draw_circle)

points = []

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        points.append([mouseX, mouseY])
        print(mouseX,mouseY)
print(points)