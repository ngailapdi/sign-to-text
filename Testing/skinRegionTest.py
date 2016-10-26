import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2        		                 
import numpy                            #importing libraries


min_YCrCb = numpy.array([0,133,77],numpy.uint8)
max_YCrCb = numpy.array([255,173,127],numpy.uint8)
cap = cv2.VideoCapture(0)                #creating camera object
while( cap.isOpened() ) :
       ret,img = cap.read()                         #reading the frames
       if img is not None:
              flip_image = img.copy()
              flip_image = cv2.flip(img,1)
       else:
       	flip_image = img

       #Image in YCrCb Color
       img = cv2.cvtColor(flip_image, cv2.COLOR_BGR2YCR_CB)
       skinRegion = cv2.inRange(img, min_YCrCb, max_YCrCb)
       contours, hierarchy =  cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

       # Draw the contour on the source image
       for i, c in enumerate(contours):
              area = cv2.contourArea(c)
              if area > 1000:
                     cv2.drawContours(img, contours, i, (0, 255, 0), 3)
       cv2.imshow('flip', img)                  #displaying the frames
       k = cv2.waitKey(10)
       if k == 27:
              cv2.imwrite('testimg.png', img)
              break
