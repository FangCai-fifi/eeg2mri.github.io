import os
import sys
import shutil
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"
ses_num = ['ses-11','ses-12','ses-21','ses-22']
c1 = 0
c2 = 0
for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts = root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if (parts[-1] == 'anat' and parts[-2] in ses_num):
        print('files:', files)
        file_num = len(files)
        for filename in files:
            part = filename.split('_')
            if part[-2] in ['ses-1', 'ses-2']:
                del_file = f"{root}/{filename}"
                print('del_file:', del_file)
                c1 = c1 + 1
                os.remove(del_file)      

    # if parts[-1] == 'anat':
    #     print('files:', files)
    #     file_num = len(files)
    #     for filename in files:
    #         part = filename.split('_')
    #         if part[-2] in ['ses-1', 'ses-2']:
    #             del_file = f"{root}/{filename}"
    #             print('del_file:', del_file)
    #             c1 = c1 + 1
    #             os.remove(del_file)    
