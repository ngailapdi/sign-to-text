import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG2()
while(1):
    ret, img = cap.read()
    if img is not None:
        flip_image = img.copy()
        flip_image = cv2.flip(img,1)
    else:
        flip_image = img
    img = flip_image
    cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
    crop_img = img[100:400, 100:400]
    thresh1 = fgbg.apply(crop_img)
    #contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
     #   cv2.CHAIN_APPROX_NONE)
    
    cv2.imshow('Thresholded',thresh1)
    cv2.imshow('Input', img)
    k = cv2.waitKey(30) & 0xffapp
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()