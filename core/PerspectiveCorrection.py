import cv2
import numpy as np

class PerspectiveCorrection:

    def transform(resizedImage,points):

        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [512, 0], [0, 512], [512, 512]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        corrected = cv2.warpPerspective(resizedImage, matrix, (512, 512))
        return corrected