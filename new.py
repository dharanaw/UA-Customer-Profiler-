import cv2
import numpy as np
from matplotlib import pyplot as plt 

face_cascade = cv2.CascadeClassifier('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/haarcascade_frontalface_default.xml')

#img_rgb = cv2.imread('/Users/dharanaweerasinghe/Desktop/Kaino/UA Files/Sample_01/mum.jpg')
#img_gray =cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#templ =cv2.imread('/Users/dharanaweerasinghe/Desktop/Kaino/UA Files/templates/1.jpg', 0)
#h, w =templ.shape[::]

#res =cv2.matchTemplate(img_gray, templ, cv2.TM_SQDIFF)

#plt.imshow(res, cmap='gray')

#min_val, max_val, min_loc, max_loc =cv2.minMaxLoc(res)  

#top_left =min_loc
#bottom_right =(top_left[0]+w, top_left[1] +h)
#cv2.rectangle(img_gray, top_left, bottom_right, 255, 2)

#cv2.imshow('matched image', img_gray)
#cv2.waitKey()
#cv2.destroyAllWindows()

img = cv2.imread('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/test images/NIC_01.JPG')
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces =face_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey()

#this is how the face is recognised with opencv 
#train/ fine tune the font for the old NIC font 
