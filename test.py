import core.Pipeline as pipe
import cv2
import multiprocessing
from time import sleep

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

points = tuple(i for i in points)
# print(points)
# print(len(points))

reference = 0
while True:
    sleep(10)
    p2 = multiprocessing.Process(target=pipe.Pipeline.process, args= ["_",points])
    p2.start()
    p2.join()
    print()
    reference += 1
    if reference == 10:
        break