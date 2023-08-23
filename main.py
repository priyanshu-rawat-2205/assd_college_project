import core.DetectTarget
import core.Capture 
import argparse
import multiprocessing
import core.Pipeline
import os.path
import time
import cv2

parser = argparse.ArgumentParser(description="Automatic shooting score detection developed by Priyanshu Rawat")

parser.add_argument("-f", "--frame", action="store_true", help="set frame corner points")
parser.add_argument("-m", "--monitor", action="store_true", help="monitor camera device feed")
parser.add_argument("-t", "--test", action="store_true", help="test current pipeline")

args = parser.parse_args()

capture = core.Capture.Capture()

if args.monitor:
    capture.getVideo(2)

if args.frame:
    # capture.captureImage(0)
    temp = cv2.imread("images/temp/temp.jpg")
    Target = core.DetectTarget.DetectTarget(temp)
    points = Target.returnPoints()
    print(points)

if args.test:
    count = 0
    lines = []
    points = []
    with open('core/temp/points.txt', 'r') as file:
        while line := file.readline():
            if not line:
                continue
            if count == 2:
                points.append(lines)
                count = 0
                lines = []
            lines.append(int(line.strip()))
            count += 1
        points.append(lines)
    tuple(points)
    print(points)
    p1 = multiprocessing.Process(target=capture.videoCaptureFrame, args=[2])

    p1.start()

    while True:
        time.sleep(3)
        p2 = multiprocessing.Process(target=core.Pipeline.Pipeline.process, args= ["_",points])
        p2.start()
        p2.join()
    


