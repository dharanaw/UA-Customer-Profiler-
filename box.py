import pytesseract
from pytesseract import Output
import cv2
import numpy as np
import math
from scipy import ndimage
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'



input_img =cv2.imread('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/test images/completebiodata.jpg')

# ORIENTATION CORRECTION/ADJUSTMENT

#####################################################################





# REGION OF INTEREST (ROI) SELECTION

# initializing the list for storing the coordinates 
coordinates = [] 
  
# Defining the event listener (callback function)
def shape_selection(event, x, y, flags, param): 
    # making coordinates global
    global coordinates 
  
    # Storing the (x1,y1) coordinates when left mouse button is pressed  
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
  
    # Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
  
        # Drawing a rectangle around the region of interest (roi)
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,0,255), 2) 
        cv2.imshow("image", image) 
  
  
# load the image, clone it, and setup the mouse callback function 
image = input_img
image_copy = input_img.copy()
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 
  
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    if key==13: # If 'enter' is pressed, apply OCR
        break
    
    if key == ord("c"): # Clear the selection when 'c' is pressed 
        image = image_copy.copy() 
  
if len(coordinates) == 2: 
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                               coordinates[0][0]:coordinates[1][0]] 
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_roi) 
    cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows()  
    









"""
config = ('-l sin --oem 1 --psm 3')

d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)
keys= list(d.keys())
n_boxes =len(d['level'])
for i in range(n_boxes):
    x,y,w,h,=d['left'][i], d['top'][i], d['width'][i], d['height'][i]
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255,),7)

    


cv2.imshow('image', img)
cv2.waitKey(0)"""