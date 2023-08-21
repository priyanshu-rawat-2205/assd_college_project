import cv2
import random as rand

FRAME_WIDTH=3
FRAME_HEIGHT=4
FRAME_RATE=5
BRIGHTNESS=10
CONTRAST=11
SATURATION=12
HUE=13
GAIN=14
EXPOSURE=15


#Opens the first imaging device
cap = cv2.VideoCapture(2) 

#Check whether user selected camera is opened successfully.
if not (cap.isOpened()):
 print("Could not open video device")

#To set the resolution
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('U', 'Y', 'V', 'Y'))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Width = ",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height = ",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Framerate = ",cap.get(cv2.CAP_PROP_FPS))
print("Format = ",cap.get(cv2.CAP_PROP_FORMAT))

Brightness=cap.get(cv2.CAP_PROP_BRIGHTNESS)
Contrast=cap.get(cv2.CAP_PROP_CONTRAST)
Saturation=cap.get(cv2.CAP_PROP_SATURATION)
Gain=cap.get(cv2.CAP_PROP_GAIN)
Hue=cap.get(cv2.CAP_PROP_HUE)
Exposure=cap.get(cv2.CAP_PROP_EXPOSURE)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('preview',frame)
#Waits for a user input to quit the application
    k = cv2.waitKey(1)
    if (k == 27):#Esc key to quite the application 
        break
    elif k == ord('g'):
        print("******************************")
        print("Width = ",cap.get(FRAME_WIDTH))
        print("Height = ",cap.get(FRAME_HEIGHT))
        print("Framerate = ",cap.get(FRAME_RATE))
        print("Brightness = ",cap.get(BRIGHTNESS))
        print("Contrast = ",cap.get(CONTRAST))
        print("Saturation = ",cap.get(SATURATION))
        print("Gain = ",cap.get(GAIN))
        print("Hue = ",cap.get(HUE))
        print("Exposure = ",cap.get(EXPOSURE))
        print("******************************")  

    elif k == ord('w'):
        if(Brightness <= 0):
            Brightness = 0
        else:
            Brightness-=10
        cap.set(BRIGHTNESS,Brightness)
        print(Brightness)
    elif k == ord('s'):
        if(Brightness >= 255):
            Brightness = 255
        else:
            Brightness+=10
        cap.set(BRIGHTNESS,Brightness)
        print(Brightness)

    elif k == ord('e'):
        if(Contrast <= 0):
            Contrast = 0
        else:
            Contrast-=10
        cap.set(CONTRAST,Contrast)
        print(Contrast)
    elif k == ord('d'):
        if(Contrast >= 255):
            Contrast = 255
        else:
            Contrast+=10
        cap.set(CONTRAST,Contrast)
        print(Contrast)

    elif k == ord('r'):
        if(Saturation <= 0):
            Saturation = 0
        else:
            Saturation-=10
        cap.set(SATURATION,Saturation)
        print(Saturation)
    elif k == ord('f'):
        if(Saturation >= 255):
            Saturation = 255
        else:
            Saturation+=10
        cap.set(SATURATION,Saturation)
        print(Saturation)

    elif k == ord('y'):
        if(Exposure <= 0):
            Exposure = 0
        else:
            Exposure-=1
        cap.set(EXPOSURE,Exposure)
        print(Exposure)
    elif k == ord('h'):
        if(Exposure >= 255):
            Exposure = 255
        else:
            Exposure+=1
        cap.set(EXPOSURE,Exposure)
        print(Exposure)

    elif k == ord('m'):
        cv2.imwrite(f"web_{rand.randint(1,10000)}.jpg",frame)
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 