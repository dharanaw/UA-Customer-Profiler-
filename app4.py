from csv import reader
import difflib
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
import pathlib
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
import os
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
config2 = ('-l eng+sin --oem 1 --psm 3')

#temp locations
dir_path= r'/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp'






def save_uploadedfile(uploaded_file):
    with open(os.path.join("temp/", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())



st.title('KYC automation v4')

uploads=st.file_uploader('upload',accept_multiple_files=True)
for files in uploads:
    if uploads is not None:
        save_uploadedfile(files)
        
        










    file_bytes = np.asarray(bytearray(files.read()), dtype=np.uint8)
    global opencv_image
    opencv_image = cv2.imdecode(file_bytes, 1)
            
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

                #thresholding
        
    thresh = cv2.threshold(gray, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                #cv2.imshow("Otsu", thresh)

                
    dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
                
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    dist = (dist * 255).astype("uint8")
            
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

    pytext = pytesseract.image_to_string(result, config=config2)
    pytext=pytext.lower()
    pytext=(pytext.replace("—‘", " "))
    pytext=pytext.translate(str.maketrans('', '', string.punctuation))
    textlines = pytext.split('\n')
    textlines = pytext.split(' ')
    textlines = [line.lower().strip() for line in textlines]


    dl_words= ('driving')
    nic_words=('national')
    proposal_words=('proposal')
    financial_words=('financial','review')

    if dl_words in pytext:
        st.write('dl detected')
    elif nic_words in pytext:
        st.write('nic detected')



    res =[]

        
            


