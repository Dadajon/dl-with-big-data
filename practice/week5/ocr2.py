import sys
import numpy as np
import cv2

im = cv2.imread('data/numbers/numbers100.png')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

contours = cv2.findContours(
    thresh,      
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)[0]

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if h < 10: continue 
    cv2.rectangle(im, (x, y), (x+w, y+h), (0,0,255), 2)
cv2.imwrite('data/numbers/numbers100-cnt2.png', im)

