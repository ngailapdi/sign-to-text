import sys

import numpy as np
import cv2

im = cv2.imread('./img/fingers.png')
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
value = (35, 35)
blurred = cv2.GaussianBlur(grey, value, 0)
_, thresh = cv2.threshold(blurred, 150, 255,
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


#################      Now finding Contours         ###################

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key= lambda x:cv2.contourArea(x))

samples =  np.empty((0,100))
print(samples) 
responses = []
keys = [i for i in range(48,58)]

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)

        if  h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            cv2.imshow('norm',im)
            key = cv2.waitKey(0)

            if key == 27:  # (escape to quit)
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1,100))
                samples = np.append(samples,sample,0)

responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))
print "training complete"

np.savetxt('./ml_data/generalsamples.data',samples)
np.savetxt('./ml_data/generalresponses.data',responses)