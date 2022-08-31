from csv import reader
import difflib
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
import pyexpat
from tkinter import Button
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




header =st.header ('KYC automation')

#getting user inputs
nic_no = st.text_input('NIC/DL number',)
nic_no=nic_no.lower()
full_name =st.text_input('Full name as in NIC/DL')
full_name=full_name.lower()
address =st.text_input('Address')
address=address.lower()
address=address.translate(str.maketrans('', '', string.punctuation))


date_of_birth =st.text_input('Date of Birth')
date_of_birth=date_of_birth.translate(str.maketrans('', '', string.punctuation))

st.write ('You entered :' + nic_no, full_name, address, date_of_birth)

config2 = ('-l eng+sin --oem 1 --psm 3')


#getting user documents 
usr_nicfront = st.sidebar.file_uploader("NIC/DL front page", type="jpg")
usr_nicback = st.sidebar.file_uploader("NIC back page", type="jpg")
usr_application = st.sidebar.file_uploader("application", type='pdf' )
usr_signature = st.sidebar.file_uploader("Signature")
usr_finance = st.sidebar.file_uploader("Supporting Financial document")

def main():
    if usr_nicfront is not None:
        file_bytes = np.asarray(bytearray(usr_nicfront.read()), dtype=np.uint8)
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

        #text extract
        pytext = pytesseract.image_to_string(result, config=config2)
        pytext=pytext.lower()
        pytext=(pytext.replace("—‘", " "))
        pytext=pytext.translate(str.maketrans('', '', string.punctuation))
        textlines = pytext.split('\n')
        textlines = pytext.split(' ')
        textlines = [line.lower().strip() for line in textlines]




    if usr_nicback is not None:
        file_bytes_back = np.asarray(bytearray(usr_nicback.read()), dtype=np.uint8)
        global opencv_image_back
        opencv_image_back = cv2.imdecode(file_bytes_back, 1)
        gray_back = cv2.cvtColor(opencv_image_back, cv2.COLOR_BGR2GRAY)

            #thresholding
    
        thresh_back = cv2.threshold(gray_back, 0, 255,
            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            
        dist_back = cv2.distanceTransform(thresh_back, cv2.DIST_L2, 5)
           
        dist_back = cv2.normalize(dist_back, dist_back, 0, 1.0, cv2.NORM_MINMAX)
        dist_back = (dist_back * 255).astype("uint8")
            #cv2.imshow("Dist", dist)
            # threshold the distance transform using Otsu's method
        #dist = cv2.threshold(dist, 0, 255,
        #       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            #cv2.imshow("Dist Otsu", dist)

            # apply an "opening" morphological operation to disconnect components
            # in the image
        kernel_back = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        opening_back = cv2.morphologyEx(dist_back, cv2.MORPH_OPEN, kernel_back)
            #cv2.imshow("Opening", opening)
        blur_back = cv2.GaussianBlur(thresh_back, (3,3), 0)
        result_back = 255 - blur_back

        #text extract
        pytext = pytesseract.image_to_string(result, config=config2)
        pytext=pytext.lower()
        pytext=(pytext.replace("—‘", " "))
        pytext=pytext.translate(str.maketrans('', '', string.punctuation))
        textlines = pytext.split('\n')
        textlines = pytext.split(' ')
        textlines = [line.lower().strip() for line in textlines]

        pytext_back = pytesseract.image_to_string(result_back, config=config2)
        pytext_back=pytext_back.lower()
        pytext_back=(pytext_back.replace("—‘", " "))
        pytext_back=pytext_back.translate(str.maketrans('', '', string.punctuation))
        textlines_back = pytext_back.split('\n')
        textlines_back = pytext_back.split(' ')
        textlines_back = [line.lower().strip() for line in textlines_back]





        dl_words= ('driving')
        nic_words=('national')

        #st.write(pytext)
        #st.write(pytext_back)
        if b: 
            if dl_words in pytext:
                st.write('Driving Licence detected')
                if not nic_no:
                    st.write('please enter the NIC no')
                else:
                    if nic_no in(pytext):
                        st.write('NIC number matched')
                    else:
                        st.write('NIC does not match')
                if not full_name:
                    st.write('please enter the full name')
                else:
                    if full_name in(pytext):
                        st.write('Full name matched')
                    else:
                        st.write('Full name does not match')
                if not address:
                    st.write('Please enter the address')
                else:
                    if address in (pytext):
                        st.write('address matched')
                        seq=difflib.SequenceMatcher(None,pytext,address)
                        d=seq.ratio()*100
                        st.write(d)
                    else:
                        st.write('address does not match')
                if not date_of_birth:
                    st.write('please enter the DOB')
                else: 
                    if date_of_birth in(pytext):
                        st.write('DOB matched')
                    else:
                        st.write('DOB does not match')
            #NIC
            elif nic_words in pytext:
                st.write('NIC detected')
                if not nic_no:
                    st.write('Please enter the NIC no')
                else:
                    if nic_no in pytext:
                        st.write('NIC number matched')
                    else:
                        st.write('NIC does not match')
                if not full_name:
                    st.write('please enter the full name')
                else:
                    if full_name in(pytext):
                        st.write('Full name matched')
                    else:
                        st.write('Full name does not match')
                if not address:
                    st.write('Please enter the address')
                else:
                    if address in (pytext_back):
                        st.write('address matched')
                        seq=difflib.SequenceMatcher(None,pytext_back,address)
                        d=seq.ratio()*100
                        st.write(d)
                    else:
                        st.write('address does not match')
                if not date_of_birth:
                    st.write('please enter the DOB')
                else: 
                    if date_of_birth in(pytext):
                        st.write('DOB matched')
                    else:
                        st.write('DOB does not match')

                
            else:
                st.write('nothing is detected')



        #for word in textlines:
         #   if word in('driving'):
          #      st.write('DL detected')

           # elif word in ('national', 'identity'):
            #    st.write('NIC detected')
            #else:
             #   st.write('cannot detect anything')











b=st.button('match')
main()  

        











