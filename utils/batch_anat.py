import os
import sys
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts=root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1]=='anat_1':
        new_r = "/".join(parts[:-1])
        print('new_r:', new_r)
        new_d = f"{new_r}/anat"
        print('new_d:', new_d)
        os.rename(root, new_d)
        
        if 'anat.nii.gz' in files:
            old_f = f"{new_d}/anat.nii.gz"
            print('old_f:', old_f)
            new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
            print("new_f:", new_f)
            os.rename(old_f, new_f)
