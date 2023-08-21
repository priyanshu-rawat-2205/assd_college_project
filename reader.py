import cv2
import numpy as np

img = cv2.imread("images/u_sheet3.jpeg")

img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow(img)