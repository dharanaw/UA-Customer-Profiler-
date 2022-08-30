import datetime
from distutils.command.upload import upload
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from matplotlib import container
import streamlit as st
from streamlit.components.v1 import iframe
from time import sleep
import time


st.set_page_config(layout="centered", page_title="KYC Automation")
st.title("Know Your Customer automation")
#st.caption('This app automate the underwriting process')

#st.write("This app automate the underwriting process")

left, padding, right = st.columns((15,2,15))

right.subheader('Document Upload')

#right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
#template = env.get_template("template.html")


left.subheader("Fill in the data:")
form = left.form("template_form")
name = form.text_input("Full Name")
nic_no = form.text_input('NIC number')
address= form.text_input('Address')
#dob = form.date_input('Date of Birth')
dob= form.date_input("Select date", value = datetime.date(2000, 1, 1), 
                          min_value = datetime.date(1940, 1, 1), 
                          max_value = datetime.date(2022, 12, 31))


sub= form.form_submit_button()
if sub:
    st.write('your details recorded successfully')



uploaded_file = right.file_uploader("", accept_multiple_files=True)
    #st.balloons()







sub_button=right.button('submit')

if sub_button:

    with st.spinner('Please wait..'):
                sleep(3)
                right.write('DL detected ✓')
                sleep(0.5)
                right.write('Proposal detected ✓')
                sleep(1.5)
                right.write('Financial review form detected ✓')
                sleep(1)
                right.write('Signature card ✓')
                #st.balloons()
        
                    
                    
                    
match_button=right.button('match')


container=st.container()
if match_button:
    container.title('results')
    with st.spinner('Please wait'):
        sleep(1)
        st.write('Full name matched')
        st.caption(name +' 100%')
        sleep(2)
        st.write('NIC number matched')
        st.caption(nic_no +'  100%')
        sleep(3)
        st.write('Address matched')
        st.caption(address+' 67%')
        sleep(0.5)
        st.write('Date of Birth matched ')
        st.caption(dob)
        st.balloons()
        



    
        
            
                    

                
    

#upload=right.button('upload')

#right.file_uploader('upload documents', accept_multiple_files=True)
#if right.file_uploader is not None:
#    right.button('match')

    
    #st.success('uploaded')
    #pdf = pdfkit.from_string(html, False)
    #st.balloons()

    #right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    #right.download_button(



