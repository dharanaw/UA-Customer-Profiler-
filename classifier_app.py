# Core Pkgs
import streamlit as st 
import cv2
from PIL import Image
import numpy as np 
import os
import fitz
import shutil
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
#temp locations
pages="temp/images/pdf_pages"
output_nic="output/nic"
output_paysheet="output/paysheets"
os.makedirs(pages,exist_ok=True)
os.makedirs(output_nic,exist_ok=True)
os.makedirs(output_paysheet,exist_ok=True)



face_cascade =cv2.CascadeClassifier("src/haarcascade_profileface.xml")

def detect_faces(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	return img,faces 

def pdf2_image(path):
    pages_paths=[]
    doc = fitz.open(path)
    zoom = 2 # to increase the resolution
    mat = fitz.Matrix(zoom, zoom)
    noOfPages = doc.pageCount
    image_folder = 'temp/images/pdf_pages/'

    for pageNo in range(noOfPages):
        page = doc.loadPage(pageNo) #number of page
        pix = page.getPixmap(matrix = mat)
    
        output = image_folder + str(pageNo) + '.jpg' 
        pix.writePNG(output)
        pages_paths.append(output)
        
    return pages_paths

def files_count():
	nic_count=len(os.listdir(output_nic))
	paysheet_count=len(os.listdir(output_paysheet))
	return nic_count,paysheet_count


#save upload file as tempory
def save_uploadedfile(uploaded_file):
    with open(os.path.join("temp/", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def main():
	
		st.header("Document Classifier")
		st.write("This application will Classify NIC and Paysheets and saveing with the proper naming convention.")
		file = st.file_uploader("Choose your file",type=["pdf","jpg","png"])
		if file is not None:
			st.info("File Uploaded Successfully")
			save_uploadedfile(file)

	 
		btn=st.button("Rename")
		# exsiting_nic,exsiting_paysheet=files_count()
		if file is not None:
			path = "temp/" + file.name
			images=pdf2_image(path)
			if btn:
				for path in images:
					our_image = Image.open(path)
					#text extract
					text = pytesseract.image_to_string(Image.open(path), lang="eng")
					textlines = text.split('\n')
					textlines = text.split(' ')
					textlines = [line.lower().strip() for line in textlines]
					paysheet=False
					for word in textlines:
						if word in ("epf","salary","allowance","total","amount","sum","payroll","paybill","deduction","tax","pay","employee"):
							paysheet=True
					#face Detection
					result_img,result_faces = detect_faces(our_image)
					if len(result_faces)>0:
						exsiting_nic=files_count()[0]
						our_image.save(output_nic+"/nic_front_side_"+str(exsiting_nic+1)+"."+file.name.split(".")[1])
						st.subheader("NIC Front Side")
						st.image(result_img)
					elif paysheet==False:
						exsiting_nic=files_count()[0]
						our_image.save(output_nic+"/nic_back_side_"+str(exsiting_nic+1)+"."+file.name.split(".")[1])
						st.subheader("NIC Back Side")
						st.image(result_img)
					#paysheet	
					if paysheet==True:
						exsiting_paysheet=files_count()[1]
						our_image = Image.open(path)
						our_image.save(output_paysheet+"/paysheet_"+str(exsiting_paysheet+1)+"."+file.name.split(".")[1])
						st.subheader("Paysheet")
						st.image(our_image)
					
 	

if __name__ == '__main__':
		main()
		shutil.rmtree('temp')	