from csv import reader
import pyexpat
from unittest import result
from cv2 import THRESH_TRUNC
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/bin/tesseract'
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


#getting user inputs

header =st.header ('KYC automation')


nic_no = st.text_input('NIC/DL number',)
full_name =st.text_input('Full name as in NIC/DL')
address =st.text_input('Address')
date_of_birth =st.date_input('Date of Birth')

st.write ('You entered :' + nic_no, full_name, address, date_of_birth)







config2 = ('-l eng --oem 1 --psm 6')
#getting user documents 
def main():

    
    uploaded_file = st.file_uploader("Choose a image file", type="jpg")

    if uploaded_file is not None:
        #Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        global opencv_image
        opencv_image = cv2.imdecode(file_bytes, 1)
        #st.sidebar.button('bounding boxes')
        #d = pytesseract.image_to_data(opencv_image, output_type=Output.DICT)
        #n_boxes = len(d['level'])
        #for i in range(n_boxes):
        #    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        #    cv2.rectangle(opencv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

            #thresholding
    
        thresh = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            #cv2.imshow("Otsu", thresh)

            # apply a distance transform which calculates the distance to the
            # closest zero pixel for each pixel in the input image
        dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
            # normalize the distance transform such that the distances lie in
            # the range [0, 1] and then convert the distance transform back to
            # an unsigned 8-bit integer in the range [0, 255]
        dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
        dist = (dist * 255).astype("uint8")
            #cv2.imshow("Dist", dist)
            # threshold the distance transform using Otsu's method
        #dist = cv2.threshold(dist, 0, 255,
        #       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            #cv2.imshow("Dist Otsu", dist)

            # apply an "opening" morphological operation to disconnect components
            # in the image
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)
            #cv2.imshow("Opening", opening)
        blur = cv2.GaussianBlur(thresh, (3,3), 0)
        result = 255 - blur

    
   # if not full_name:
    #    st.write('please enter full name')
    #if not address:
     #   st.write('please enter address')
    #if not date_of_birth:
     #   st.write('please enter date of birth')




        button=st.button('match')
        if button:
            pytext = pytesseract.image_to_string(result, config=config2)
            #st.write (pytext)

            textlines = pytext.split('\n')
            textlines = pytext.split(' ')
            textlines = [line.lower().strip() for line in textlines]
            driving_license = False

            for word in textlines:
                if word in ('driving','license'):
                    driving_license =True
                    st.write ('license detected')
                
            if not nic_no:
                st.write('please enter NIC no')
            else:
                for nic_no in pytext:
                    if nic_no in (nic_no):
                        st.write('NIC matched')
               # if not nic_no:
                #    st.write ('please input NIC no')
                #if nic_no in pytext:
                 #   st.write('NIC/DL matched')
            


            #if nic_no in pytext:
             #   st.write('NIC/DL matched')
            #else:
             #   st.write('NIC no does not match') 
                

            





                    #nam =textlines.find(full_name)
                    #st.write()

                        

                
            
            #elif word in ('')
               # else:
                #    st.write('Dl not detected')
                 #   break

                
                        
                         

                            

                        



            #face Detection
            

            




        #Now do something with the image! For example, let's display it:
            #st.image(opencv_image, channels="BGR")
            







        
        
	
main()		


