import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import math
import time
cap = cv2.VideoCapture(0)
frameNum = 0
start = time.time()
while(cap.isOpened()):
	ret,img = cap.read()                         #reading the frames

	frameNum += 1
	if frameNum == 100:
		break
end = time.time()
print(end-start)