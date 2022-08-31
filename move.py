import os
import shutil


src='/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp'
dest='/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp/jpg'
dest2='/Users/dharanaweerasinghe/Desktop/pythonProject/nic_transcriber/temp/pdf'
for root,dirs,files in os.walk(src):
    for file in files:
        if file.endswith('.jpg'):
            shutil.move(os.path.join(root,file), os.path.join(dest,file))
            print('moved successfully')
        
