import core.Capture as cap
import core.DetectTarget as dt
import core.PerspectiveCorrection as pcr
import core.ImageEnhancer as ie
import core.ImageUtility as iu
import core.ShotDetector as sd
import core.Score as scr
import cv2

if __name__ == "__main__":

    image = cap.Capture()
    image.captureImage(0)
    # temp = cv2.imread("images/temp/temp.jpg")
    temp = cv2.imread("images/example/web_9972.jpg")
    cleanTarget = cv2.imread("images/example/cleanTarget.jpg")

    corner = dt.DetectTarget(temp) #points list will be checked for null to make this execute only during initialization
    resizedImage = iu.ImageUtility.image_resize(temp, 512, 512)
    points = corner.returnPoints()
    corrected = pcr.PerspectiveCorrection.transform(resizedImage, points)

    enhancer = ie.ImageEnhancer(corrected)
    enhanced = enhancer.returnEnhanced()

    shot = sd.ShotDetector(enhanced, corrected, cleanTarget)
    shotPoints = shot.returnShotPoints()
    shotImage = shot.returnShotImage()
    shotTarget = shot.returnShotTarget()

    cv2.imwrite("images/out/shotTarget.jpg", shotTarget)

    score = scr.Score(shotPoints)
    final = score.finalScore()
    scoreCm = score.returnDist()
    print(final)

    cv2.imshow("test", shotImage)
    cv2.waitKey(0)