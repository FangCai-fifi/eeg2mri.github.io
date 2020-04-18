import os
import sys
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"
dwi_name = ['dti.bval','dti.bvec','dti.nii.gz']

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts=root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1]=='dti_1':
        new_r = "/".join(parts[:-1])
        print('new_r:', new_r)
        new_d = f"{new_r}/dwi"
        print('new_d:', new_d)
        os.rename(root, new_d)
        
        for filename in files:
            if filename == dwi_name[0]:
                old_f = f"{new_d}/{filename}"
                print('old_f:', old_f)
                new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.bval"
                print("new_f:", new_f)
                os.rename(old_f, new_f)
            if filename == dwi_name[1]:
                old_f = f"{new_d}/{filename}"
                print('old_f:', old_f)
                new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.bvec"
                print("new_f:", new_f)
                os.rename(old_f, new_f)
            if filename == dwi_name[2]:
                old_f = f"{new_d}/{filename}"
                print('old_f:', old_f)
                new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.nii.gz"
                print("new_f:", new_f)
                os.rename(old_f, new_f)