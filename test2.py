from csv import reader
import difflib
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
import string
from difflib import SequenceMatcher
from pyzbar import pyzbar 
from pyzbar.pyzbar import decode 
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
nic_no=nic_no.lower()
full_name =st.text_input('Full name as in NIC/DL')
full_name=full_name.lower()
address =st.text_input('Address')
address=address.lower()
address=address.translate(str.maketrans('', '', string.punctuation))


date_of_birth =st.text_input('Date of Birth DD.MM.YYYY')
date_of_birth=date_of_birth.translate(str.maketrans('', '', string.punctuation))

st.write ('You entered :' + nic_no, full_name, address, date_of_birth)

config2 = ('-l eng+sin --oem 1 --psm 3')
#getting user documents 

uploaded_file = st.file_uploader("Choose a image file", type="jpg")
uploaded_file_back = st.file_uploader("back page of NIC", type="jpg")


if uploaded_file_back is not None:
    global opencv_image_back
    file_bytes_back= np.asarray(bytearray(uploaded_file_back.read()), dtype=np.uint8)
    opencv_image_back=cv2.imdecode(file_bytes_back, 1)




def char_extract():
    pytext = pytesseract.image_to_string(result, config=config2)
    #pytext_back = pytesseract.image_to_string(opencv_image_back, config=config2)

    #pytext_back=pytext_back.lower()
    #pytext_back=(pytext_back.replace("—‘", " "))
    #pytext_back=pytext_back.translate(str.maketrans('', '', string.punctuation))



    pytext=pytext.lower()
    pytext=(pytext.replace("—‘", " "))
    pytext=pytext.translate(str.maketrans('', '', string.punctuation))
    
    
    st.write (pytext)
    #st.write(pytext_back)

    textlines = pytext.split('\n')
    textlines = pytext.split(' ')
    textlines = [line.lower().strip() for line in textlines]

    if not nic_no:
        st.write('please enter the nic no')
    else:
        if nic_no in (pytext):
            st.write(nic_no+ ': nic matched')
        else:
            st.write('nic does not match')
        
    if not full_name:
        st.write('please enter the full name')
    else:
        if full_name in(pytext):
            st.write('name matched')
        else:
            st.write('name does not match')

    if not address:
        st.write('please enter the address ')
    else:
     #   if address in (pytext_back):
      #      st.write('address matched')
       # else:
            seq=difflib.SequenceMatcher(None,pytext,address)
            d=seq.ratio()*100
            st.write(d)
   
   # else:
    #    seq=difflib.SequenceMatcher(None, pytext,address)
     #  d=seq.ratio()*100
      #  st.write(d)
    
    if not date_of_birth:
        st.write('Please enter the birthday')
    else:
        if date_of_birth in (pytext):
            st.write('Date of Birth Matched')
        else:
            st.write('Date of Birth does not match')

        


    # Make one method to decode the barcode
def BarcodeReader():
     
    # read the image in numpy array using cv2
    #img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(result)
      
    # If not detected then print the message
    if not detectedBarcodes:
        st.write("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to heighlight the barcode
            cv2.rectangle(result, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                st.write(barcode.data)
                st.write(barcode.type)
                 
    #Display the image
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

















if uploaded_file  is not None:
        
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
            char_extract()
            #BarcodeReader()
            
        #driving_license = False

            
                



                
            
                
        
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
            


