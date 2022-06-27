from csv import reader
from unittest import result
from cv2 import THRESH_TRUNC
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'
import cv2 
from cv2 import cvtColor
import re
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import pandas as pd 
from PIL import Image
import streamlit as st
from io import StringIO
import easyocr 
from IPython.display import display
from pytesseract import Output
import imutils
import ssl
import googletrans
from googletrans import Translator


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context



#PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
#ID_REG = re.compile(r'[a-z0-9\.\-+_]+V\v')

#def extract_id(id_text):
#    return re.findall(ID_REG, id_text)


#def extract_phone_number(resume_text):
#    phone =re.findall(PHONE_REG, resume_text)
#    if phone:
#        number =''.join(phone[0])
#        if resume_text.find(number) >=0 and len(number) <20:
#             return number
#    return None      """   

#xyz =st.file_uploader("Choose a file")


#easyOCR 
 
"""
imagepath ='british.png'
def convert(imagepath):
    image = Image.open(imagepath)
    image = image.convert("RGBA")
    text = pytesseract.image_to_string(image, config='--psm 6')   #this config helps to read row by row
    print(text)



def getImageOrientation(image):
    try:
        orientation = str(pytesseract.image_to_osd(image)).split('\n')[1].split(':')[1]
        return orientation
    except pytesseract.pytesseract.TesseractError:  #Exception occurs on empty pages, return 0 orientation
        return 0
          
def fixOrientation(image):
    orientation = getImageOrientation(image)
    rotated = image
    if(orientation!=0):
      rotated = image.rotate(360-int(orientation))
    return rotated
          
def convert(imagepath):
    image = Image.open(imagepath)
    image = image.convert("RGBA")

    rotated = fixOrientation(image)   #fix image orientation
    text = pytesseract.image_to_string(rotated, config='--psm 6')   #this config helps to read row by row

    print(text)
"""



#uploaded_file = st.file_uploader("Choose a image file", type="jpg")

#if uploaded_file is not None:
    # Convert the file to an opencv image.
 #   file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  #  opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
   # st.image(opencv_image, channels="BGR")



# read image
im = cv2.imread('namefield.jpg')

#grayscaling
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#thresholding
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("Otsu", thresh)

# apply a distance transform which calculates the distance to the
# closest zero pixel for each pixel in the input image
dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
# normalize the distance transform such that the distances lie in
# the range [0, 1] and then convert the distance transform back to
# an unsigned 8-bit integer in the range [0, 255]
dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
dist = (dist * 255).astype("uint8")
cv2.imshow("Dist", dist)
# threshold the distance transform using Otsu's method
dist = cv2.threshold(dist, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Dist Otsu", dist)

# apply an "opening" morphological operation to disconnect components
# in the image
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
#k = cv2.waitKey(0)
#if k == 27 or k == ord('q'):
 #   cv2.destroyAllWindows()



#getting bounding boxes
#cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
#xcv =cv2.imshow('cnts' cnts)

#for c in cnts:
#    x,y,w,h, = cv2.boundingRect(c)
#    cv2.rectangle(im,(x,y),(x+w, y+h), (36,255,12)2)
#cv2.imwrite("/.out.png",im) 


#cv2.imwrite( 'boxed results.jpg' result)
#recognized = cv2.imshow('boxed',result)









"""# find contours in the opening image, then initialize the list of
# contours which belong to actual characters that we will be OCR'ing
cnts = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
chars = []
 loop over the contours
for c in cnts:
	# compute the bounding box of the contour
	(x, y, w, h) = cv2.boundingRect(c)
	# check if contour is at least 35px wide and 100px tall, and if
	# so, consider the contour a digit
	if w >= 35 and h >= 100:
		chars.append(c)"""

blur = cv2.GaussianBlur(thresh, (3,3), 0)
result = 255 - blur 

# configurations
config = ('-l sin --oem 1 --psm 3')
# pytessercat
text = pytesseract.image_to_string(result, config=config)
# print text
extracted_text = text.split('\n')
print(extracted_text )


str_value= ''.join(extracted_text)

t= Translator()

supported_langs = googletrans.LANGUAGES
#print(supported_langs)

translated_text =t.translate (str_value,src='si', dest='en')
print(translated_text)

#translated_text =t.translate ('ධාරණ දම්සර වීරසිංහ ' ,src='si', dest='en')
#print(translated_text)









