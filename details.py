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



# mapping
class sin_str(str):
    @property
    def __phonetics(self) -> dict:
        return {'සිංහ':'singhe',
                'ධා':'dha',
                'ජී':'jee',
                'ණ':'na',
                'තා':'tha',
                'ජා':'ja',
                'සු':'su',
                'වී':'wee',
                'ම්':'m',
                'ස්':'s',
                'ර්':'r',
                'හ':'ha',
                'ර':'ra',
                'ද':'da',
                'ස':'sa',
                'ව':'wa',
                'ල':'la',
                'න':'na',
                ' ':' '
               }
    
    @property
    def transliteration(self) -> str:
        p,t = self.__phonetics, self [:]
        for k,v in p.items(): t=t.replace(k, v)
        return t
        #return ''.join(p.get(c, None) or c for c in self)
        


uploaded_file = st.sidebar.file_uploader("Choose a image file", type="jpg")

if uploaded_file is not None:
     #Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    global opencv_image
    opencv_image = cv2.imdecode(file_bytes, 1)
    #st.sidebar.button('bounding boxes')
    #d = pytesseract.image_to_data(opencv_image, output_type=Output.DICT)
    #n_boxes = len(d['level'])
    #for i in range(n_boxes):
     #   (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
     #   cv2.rectangle(opencv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
   
    

    
     #Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")

else:
    st.write("Please upload the image first")
face_cascade = cv2.CascadeClassifier('/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/haarcascade_frontalface_default.xml')


if st.sidebar.button("extract and transliterate text"):   

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
        # threshold the distance transform using Otsu's method
   
        # apply an "opening" morphological operation to disconnect components
        # in the image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)
        #cv2.imshow("Opening", opening)
    blur = cv2.GaussianBlur(thresh, (3,3), 0)
    result = 255 - blur

    st.image(result)
     # configurations
    #config = r'--oem 3 --psm 6 outputbase digits -c preserve_interword_spaces=1'
    config = ('-l eng --oem 1 --psm 6 ')
            # pytessercat
    pytext = pytesseract.image_to_string(result, config=config)
    st.write('extracted text is :' + pytext)

    if st.sidebar.button('recognise face'):
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for(x, y, w, h) in faces:
            cv2.rectangle(opencv_image,(x, y), (x+w, y+h), (255, 0, 0), 2)

            st.image(cv2.imshow('img',opencv_image))
            cv2.waitKey()
  
    #alterd_pytext = pytext.replace("නම :", "")
            # print text
    #extracted_text = pytext #.split('/n')
    #print(extracted_text )
    #do nothing 


    #str_value= ''.join(extracted_text) 
    


  
  #object detection by template matching   
  
  
    #intext = sin_str(alterd_pytext)
    #st.write('Translated text is:  '+ intext.transliteration)




    #text=input('type :')
    #text = sin_str(text)
   
   
   
   
   
   
    #print(text.transliteration) 
    




#use
#st.button('transliterate to english')

#typo =st.text_input('type in sinhala')

 #takama
    



   # t= Translator()
   # supported_langs = googletrans.LANGUAGES
            #print(supported_langs)

   # translated_text =t.translate (str_value,src='si', dest='en')
    
    #st.write('Translated text is '+translated_text.text
