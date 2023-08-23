import math

class Score:

    FRAME_IN_CM = 17.8
    FRAME_IN_PX = 512
    RING_COUNT = 10
    BULLSEYE_RADIUS = 0.6
    RING_WIDTH = 0.8
    RING_PARTION_WIDTH = 0.08

    PX2CM = FRAME_IN_CM/FRAME_IN_PX
    
    def __init__(self, points, frameSize = (512, 512)):
        dist = math.dist(points[0], points[1])
        self.dist = dist * self.PX2CM

    def returnDist(self):
        return self.dist
    
    def finalScore(self):
        self.dist = round(self.dist, 2)
        if not self.dist <= 0.6:
            frac, whole = math.modf(self.dist)
            frac = round(frac, 2)
            shotRing = self.RING_COUNT - (self.dist//self.RING_WIDTH)
            ringSection = frac//self.RING_PARTION_WIDTH
            score = shotRing + (ringSection/10)
            score = round(score, 2)
            return score
        else:
            return 10