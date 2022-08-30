from csv import reader
import difflib
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from fileinput import filename
from glob import glob
import pathlib
import pyexpat
from time import sleep
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
import fitz
from pathlib import Path
import shutil
import matplotlib.image as mpimg
import glob
from datetime import date
import datetime
#temp locations
dir_path= r'/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp'
pdf_path='/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp/pdf'
jpg_path='/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp/jpg'
pdf_search=Path('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp').glob('*.pdf')
img_search=Path('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp').glob('*.jpg')
pdf_files = [str(file.absolute()) for file in pdf_search]
img_files = [str(file.absolute()) for file in img_search]

try:
    os.mkdir(dir_path)
except OSError:
    print ("Creation of the directory %s failed" )
else:
    print ("Successfully created the directory ")


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
config2 = ('-l eng+sin --oem 1 --psm 3')


    







dl_words= ('driving')
nic_words=('national')
proposal_words=('Union Life Plus Proposal Form - Extract of the details submitted on a digital proposal form')
financial_words=('PERSONAL FINANCIAL NEEDS REVIEW')

    #if dl_words in pytext:
     #   st.write('dl detected')
    #elif nic_words in pytext:
     #   st.write('nic detected')
   





def save_uploadedfile(uploaded_file):
    with open(os.path.join("temp/", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())




container=st.container()
col1, padding, col2,  = st.columns((10,2,15))

with col1:
    st.header("user inputs")
    nic_no = st.text_input('NIC/DL number',)
    nic_no=nic_no.lower()
    full_name =st.text_input('Full name as in NIC/DL')
    full_name=full_name.lower()
    address =st.text_input('Address')
    address=address.lower()
    #address=address.translate(str.maketrans('', '', string.punctuation))

    dob= st.date_input("Date of Birth", value = datetime.date(2000, 1, 1), 
                          min_value = datetime.date(1940, 1, 1), 
                          max_value = datetime.date(2022, 12, 31))
    new_dob=dob.strftime('%d/%m/%Y')
    xc=new_dob.replace('/','.')
                    
   # date_of_birth =st.text_input('Date of Birth')

    #date_of_birth=date_of_birth.translate(str.maketrans('', '', string.punctuation))

    
with col2:
    st.header('Documents upload')
    
    uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=True)
    if uploaded_file is not None:
        for files in uploaded_file:
        
            save_uploadedfile(files)
            
    else:
            st.write('please upload documents first')



ext = ['png', 'jpg' ,'jpeg']    # Add image formats here



def load_images(dir_path):
    images = []
    for filename in os.listdir(dir_path):
        img = mpimg.imread(os.path.join(dir_path, filename))
        if img is not None:
            images.append(img)
            pytext = pytesseract.image_to_string(images, config=config2)
            st.write(pytext)
     


container=st.container()
container.subheader("Results")
#if st.file_uploader is not None:
 #   st.write('sucessfully uploaded')

    # You can call any Streamlit command, including custom components:
    

#st.write("This is outside the container")









file_names =os.listdir(dir_path)
magic =col2.button('magic')
if magic:


        for pdf in pdf_files:
        
            with fitz.open(pdf) as doc:
                for page in doc:
                    text = page.get_text()
                    #st.write(text)
                    if financial_words in (text) :
                        st.write('Financial review detected')
                    elif proposal_words in (text):
                        st.write('Proposal detected')


    
    #files=glob.glob(dir_path+'/*jpg')

    
        for image in img_files:
            st.write('Identification document detected')
            for file_name in file_names:
                    #imz =Image.open(dir_path + file_name)
                    
                imz = Image.open(dir_path + '/' + file_name)

                text=pytesseract.image_to_string(imz, config=config2)
                text=text.lower()
                #text=text.translate(str.maketrans('', '', string.punctuation))
                #st.write(text)

                
                if not nic_no:
                    st.write('Please enter the nic number')
                else:
                    if nic_no in (text):
                        st.write('NIC No matched ✓')
                    else:
                        st.write('NIC does not match')
                if not full_name:
                    st.write('Please enter the full name')
                else:
                    if full_name in(text):
                        st.write('Full name matched ✓')
                    else:
                        st.write('Full name does not match')
                if not address:
                    st.write('Please enter the address')
                else:
                    if address in(text):
                        st.write('address matched ✓')
                    else:
                        st.write('address does not match')
                if not dob:
                    st.write('Please enter the birthday')
                else:
                    if xc in (text):
                        st.write('Date of Birth Matched ✓')
                    else:
                        st.write('Date of Birth does not match')
                st.balloons()



                


                      
                   
                









        
   

