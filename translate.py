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



uploaded_file = st.file_uploader("Choose a image file", type="jpg")

if uploaded_file is not None:
     #Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    global opencv_image
    opencv_image = cv2.imdecode(file_bytes, 1)

     #Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")
else:
    st.write("Please upload the image first")

if st.button("extract and translate"):   

    #text preprocessing 
        #grayscaling
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

    st.image(result)
     # configurations
    config = ('-l sin --oem 1 --psm 3')
            # pytessercat
    pytext = pytesseract.image_to_string(result, config=config)
            # print text
    extracted_text = pytext.split('/n')
    #print(extracted_text )


    str_value= ''.join(extracted_text)
    st.write(extracted_text)



# mapping
class sin_str(str):
    @property
    def __phonetics(self) -> dict:
        return {'සු':'su',
                'ජා':'ja',
                ' ':' ',
                'තා':'tha',
                'ව':'wa',
                'ර්':'r',
                'ර':'ra',
                'න':'na',
                'ල':'la',
                'තා':'tha',
                'ජී':'jee',
                'වා':'va',
                'න':'na',
                'න්':'n',
                'ද':'da',
                'ධ':'dha',
                'ණ':'na',
                'උ':'u',
                'ප':'pa',
                'ත':'tha',
                'හා':'haa',
                'ධා':'dha',
                'නා':'naa',
                'ස':'sa',
                'හෝ':'ho',
                'නි':'ni',
                'ල':'la',
                'බා':'ba',
                'ඇ':'ae',
                'ත':'tha',
                'අ':'a',
                'ඉ':'i',
                'ඊ':'ee',
                'එ':'ae',
                'ඔ':'o',
                'ක':'ka',
                'ග':'ga',
                'න':'na',
                'ත':'tha',
                'ද':'dha',
                'ඩ':'da',
                'න':'na',
                'ත':'tha',
                'ප':'pa',
                'බ':'ba',
                'ම':'ma',
                'ය':'ya',
                'ර':'ra',
                'ල':'la',
                'ව':'wa',
                'ශ':'sha',
                'ස':'sa',
                'හ':'ha',
                'ල':'la',
                'ෆ':'fa',
                'ස්':'s'}
                
                
    
    @property
    def transliteration(self) -> str:
        p = self.__phonetics
        return ''.join(p.get(c, None) or c for c in self)




#use
#st.button('transliterate to english')

typo =st.text_input('type in sinhala')
intext = sin_str(typo)
st.write(intext.transliteration) #takama
    



   # t= Translator()
   # supported_langs = googletrans.LANGUAGES
            #print(supported_langs)

   # translated_text =t.translate (str_value,src='si', dest='en')
    
    #st.write('Translated text is '+translated_text.text)

