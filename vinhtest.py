import cv2
import numpy as np

#######   training part    ############### 
samples = np.loadtxt('./ml_data/generalsamples.data',np.float32)
responses = np.loadtxt('./ml_data/generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.KNearest()
model.train(samples,responses)

############################# testing part  #########################

# im = cv2.imread('./img/fingers.png')
# out = np.zeros(im.shape,np.uint8)
# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

im = cv2.imread('./img/fingers.png')
out = np.zeros(im.shape, np.uint8)
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
value = (35, 35)
blurred = cv2.GaussianBlur(grey, value, 0)
_, thresh = cv2.threshold(blurred, 150, 255,
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
            string = str(int((results[0][0])))
            cv2.putText(out,string,(x,y+h),0,1,(0,255,0))

cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)