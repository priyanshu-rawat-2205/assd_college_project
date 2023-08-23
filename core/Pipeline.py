import cv2
import core.ImageUtility
import core.PerspectiveCorrection
import core.DetectTarget
import core.ImageEnhancer
import core.PerspectiveCorrection
import core.ShotDetector
import core.Score

class Pipeline:
    def process(self, *point):
        points = point[0]
        # points = point
        # if len(points) != 4:
        #     print("not four points")
        #     print(points)
        #     return
        # else:
        #     print ("got four")
        #     print(points)
        temp = cv2.imread("images/temp/temp.jpg")
        cleanTarget = cv2.imread("images/example/cleanTarget.jpg")
        resizedImage = core.ImageUtility.ImageUtility.image_resize(temp, 512, 512)
        resizedImage = core.ImageUtility.ImageUtility.image_resize(temp, 512, 512)
        corrected = core.PerspectiveCorrection.PerspectiveCorrection.transform(resizedImage, points)

        enhancer = core.ImageEnhancer.ImageEnhancer(corrected)
        enhanced = enhancer.returnEnhanced()

        shot = core.ShotDetector.ShotDetector(enhanced, corrected, cleanTarget)
        shotPoints = shot.returnShotPoints()
        print(shotPoints)
        if len(shotPoints) >= 2:
            if not (256, 256) in shotPoints:
                print("Error! There may be noise in the image or the center is not aligned hence the score is not accurate")
        elif len(shotPoints) ==  0:
            print("Error! No shots are detected")
            return
        else:
            if not (256, 256) in shotPoints:
                shotPoints.append((256, 256))
            else:
                print(10)
                return    


        shotImage = shot.returnShotImage()
        cv2.imshow("detected shots", shotImage)
        cv2.waitKey(0)
        shotTarget = shot.returnShotTarget()

        cv2.imwrite("images/out/shotTarget.jpg", shotTarget)

        score = core.Score.Score(shotPoints)
        finalScore = score.finalScore()
        scoreCm = score.returnDist()
        print(finalScore)
        return
        
