import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import math
import os
cap = cv2.VideoCapture(0)
frameNumber = 0
lastFive = []
lastZero = []
lastFrameDetected = -150
while(cap.isOpened()):
    frameNumber += 1
    ret, img = cap.read()
    if img is not None:
        flip_image = img.copy()
        flip_image = cv2.flip(img,1)
    else:
        flip_image = img
    img = flip_image
    cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
    crop_img = img[100:400, 100:400]
    #print crop_img.shape
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 150, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Thresholded', thresh1)

    #(version, _, _) = cv2.__version__.split('.')

    #elif version is '2':
    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
        cv2.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    
    x,y,w,h = cv2.boundingRect(cnt)

    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)

    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    #print drawing
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    if defects is not None:
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            #    cv2.putText(img, "Angle ="+ str(angle), (50,300), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            #print(angle)
            if angle <= 90:
                count_defects += 1
                #lastFrameDetected = print ("1 finger detected")
                cv2.circle(crop_img,far,1,[0,0,255],-1)
            #dist = cv2.pointPolygonTest(cnt,far,True)
            cv2.line(crop_img,start,end,[0,255,0],2)
            #cv2.circle(crop_img,far,5,[0,0,255],-1)
    if count_defects == 1:
        cv2.putText(img,"Two Fingers Detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 2:
        str = "Three Fingers Detected"
        cv2.putText(img, str, (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    elif count_defects == 3:
        cv2.putText(img,"4 Fingers Detected :P", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"FIVE!!!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        lastFive.append(frameNumber)
    else:
        cv2.putText(img,"No Fingers!!!", (50,50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        if len(lastFive)>2 and len(lastZero)>2:

            if frameNumber - lastFive[-1]<10 and abs(lastZero[-1]-lastFive[-1])<10 and frameNumber - lastFrameDetected >40 :
                    print("Goodbye")
                    os.system("say 'goodbye'")
                    lastFrameDetected = frameNumber
        lastZero.append(frameNumber)
    #cv2.imshow('drawing', drawing)
    #cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)
    k = cv2.waitKey(10)
    if k == 27:
        break