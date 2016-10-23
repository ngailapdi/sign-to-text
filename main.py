import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import math
import os

# Function to flip image in mirror effect
def flippedImage(image):
    if image is not None:
        flip_image = image.copy()
        flip_image = cv2.flip(image,1)
    else:
        flip_image = img
    return flip_image

# Background Subtraction and turn image to black-white
def blackWhiteImage(crop_img):
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 150, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh1

samples = np.loadtxt('./ml_data/magichand_samples.data',np.float32)
responses = np.loadtxt('./ml_data/magichand_responses.data',np.float32)
responses = responses.reshape((responses.size,1))
model = cv2.KNearest()
model.train(samples,responses)

# Initialization
frameNumber = 0
lastZero = []
lastOne = []
lastTwo = []
lastThree = []
lastFour = []
lastFive = []
lastFrameDetected = -50
words = {0: 'Hello', 1: 'I', 2: 'Love', 3: 'You', 5: 'Good Bye', 7: 'Hack GSU 2016'}
flag = False
#Main Function
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    
    frameNumber += 1            # Increase number of Frame

    ret, img = cap.read()   
    img = flippedImage(img)
    ## Create 2 rectangle to detect the hand
    cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
    crop_img = img[100:400, 100:400]
    cv2.imshow('Gesture', img)
    thresh1 = blackWhiteImage(crop_img)
    cv2.imshow('Thresholded', thresh1)

    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST, 
        cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    

    k = cv2.waitKey(10)
    if k == 27:
        break
    elif k == 48: 
        if flag:
            flag = False
        else:
            flag = True
    if flag and  cv2.contourArea(cnt)>5000:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>100:
            #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh1[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
            digit = int((results[0][0]))-48
            string = words[digit]
            if (dists<20 and frameNumber - lastFrameDetected >10):
                lastFrameDetected = frameNumber
                print(string)
                print(dists)
                os.system("say '{0}'".format(string)) 
            else:    
                print(dists)
 

