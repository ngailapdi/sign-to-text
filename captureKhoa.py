import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2        		                 
import numpy as np                           #importing libraries
cap = cv2.VideoCapture(0)                #creating camera object
while( cap.isOpened() ) :
       ret,img = cap.read()                         #reading the frames
       if img is not None:
       		flip_image = img.copy()
       		flip_image = cv2.flip(img, 1)
       else:
       		flip_image = img
       cv2.imshow('flip', flip_image)                  #displaying the frames
       k = cv2.waitKey(10)
       if k == 27:
       		cv2.imwrite('testimg.png', img)
       		break
