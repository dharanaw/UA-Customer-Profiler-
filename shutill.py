
   for file_name in file_names:
        if os.path.join(dir_path, file_name).endswith('.jpg'):
           shutil.move(os.path.join(dir_path, file_name), os.path.join(jpg_path,'images.jpg'))
        if os.path.join(dir_path, file_name).endswith('.pdf'):
            shutil.move(os.path.join(dir_path, file_name), os.path.join(pdf_path,'pdfs.pdf'))


    
"""for pdf in pdf_files:
    
        with fitz.open(pdf) as doc:
            for page in doc:
                text = page.get_text()
                #st.write(text)
                if financial_words in (text) :
                    st.write('Financial review detected')
                elif proposal_words in (text):
                    st.write('Proposal detected')"""
        
    