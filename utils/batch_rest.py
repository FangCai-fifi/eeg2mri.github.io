import os
import sys
import shutil
from os import path

dir = "/Users/fangcai/Downloads/data/IBA_TRT_0027223_0027233/sub-0027227"
rest_num = ['rest_1', 'rest_2']

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts = root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1] in rest_num:
        part_num = parts[-1].split('_')[-1]
        print('part_num:', part_num)
        old_r = "/".join(parts[:-1])
        print('old_r:', old_r)
        new_r = "/".join(parts[:-2])
        new_rn = f"{new_r}/{parts[-2]}{part_num}"
        print('new_r:', new_r)
        print('new_rn:', new_rn)
        os.mkdir(new_rn)
        new_df = f"{new_rn}/func"
        print('new_df:', new_df)
        new_fn = f""
        os.rename(root, new_df)

        if files[0] == 'rest.nii.gz':
            old_file = f"{new_df}/{files[0]}"
            print('old_file:', old_file)
            part = old_file.split('/')
            print('part:', part)
            new_file = f"{new_df}/{part[-4]}_{part[-3]}_task-rest_bold.nii.gz"
            print("new_file:", new_file)
            os.rename(old_file, new_file)
        
        old_a = f"{new_r}/{parts[-2]}/anat"
        new_a = f"{new_rn}/anat"
        old_af = f"{new_r}/{parts[-2]}/anat/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
        new_af = f"{new_rn}/anat/{part[-4]}_{part[-3]}_T1w.nii.gz"
        print('old_a:', old_a)
        print('new_a:', new_a)
        print('old_af:', old_af)
        print('new_af:', new_af)
        shutil.copytree(old_a, new_a)
        shutil.copyfile(old_af, new_af)
        