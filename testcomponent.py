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
import os 
import fitz

#temp locations
pages="temp/images/pdf_pages"
#output_nic="output/nic"
#output_paysheet="output/paysheets"
os.makedirs(pages,exist_ok=True)
#os.makedirs(output_nic,exist_ok=True)
#os.makedirs(output_paysheet,exist_ok=True)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context





def pdf2_image(path):
    pages_paths=[]
    doc = fitz.open(path)
    zoom = 2 # to increase the resolution
    mat = fitz.Matrix(zoom, zoom)
    noOfPages = doc.page_count
    image_folder = 'temp/images/pdf_pages/'

    for pageNo in range(noOfPages):
        page = doc.load_page(pageNo) #number of page
        pix = page.get_pixmap(matrix = mat)
    
        output = image_folder + str(pageNo) + '.jpg' 
        pix.save(output)
        pages_paths.append(output)
        
    return pages_paths


#save upload file as tempory
def save_uploadedfile(uploaded_file):
    with open(os.path.join("temp/", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())


st.title( 'KYC Automation')

#st.text(” A simple way to upload files directly into a directory”)
uploadedfiles = st.file_uploader('upload', accept_multiple_files=True)
for files in uploadedfiles:
    if uploadedfiles is not None:
        save_uploadedfile(files)
        st.write('file upload completed')
    else:
        st.write('please upload documents')
    #button=st.button('classify')
    if uploadedfiles is not None:
        path='temp/'+files.name
        images=pdf2_image(path)
        #st.button('new')
        
        for path in images:
            our_images=Image.open(path)

            #extraction
            text=pytesseract.image_to_string(Image.open(path),lang='eng')
            for word in text:
                if word in('personal','financial'):
                    st.write('Finalcial Needs Review found')
                elif word in ('proposal','form'):
                    st.write('Proposal form found')




"""im=[]
    for filename in os.listdir(dir_path):
        try:
            pic=mpimg.imread(os.path.join(dir_path, filename))
            if pic is not None:
                im.append(pic)
        except:
            print('cant import')
    picture= np.asarray(im)
    #st.image(picture)                
    pytext = pytesseract.image_to_string(pic, config=config2)
    st.write(pytext)"""




                    



