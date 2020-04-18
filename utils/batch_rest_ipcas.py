import os
import sys
import shutil
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"
rest_num = ['rest_1', 'rest_2']

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts = root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    # copy ses-x to ses_xy
    if (parts[-1] == 'rest_1'):
        part_num = parts[-1].split('_')[-1]
        print('part_num:', part_num)
        old_r = "/".join(parts[:-1])
        print('old_r:', old_r)
        new_r = "/".join(parts[:-2])
        new_r = f"{new_r}/{parts[-2]}{part_num}"
        print('new_r:', new_r)
        #os.mkdir(new_r)
        #shutil.copytree(f"{old_r}/anat", f"{new_r}/anat")
        new_f = f"{old_r}/func"
        print('new_f:', new_f)
        os.rename(root, new_f)

        if 'rest.nii.gz' in files:
            old_file = f"{new_f}/rest.nii.gz"
            print('old_file:', old_file)
            part = old_file.split('/')
            print('part:', part)
            new_file = f"{new_f}/{part[-4]}_{part[-3]}_task-rest_bold.nii.gz"
            print("new_file:", new_file)
            os.rename(old_file, new_file)

    if (parts[-1] == 'rest_2'):
        part_num = parts[-1].split('_')[-1]
        print('part_num:', part_num)
        old_r = "/".join(parts[:-1])
        print('old_r:', old_r)
        new_r = "/".join(parts[:-2])
        new_r = f"{new_r}/{parts[-2]}{part_num}"
        print('new_r:', new_r)
        os.mkdir(new_r)
        shutil.copytree(f"{old_r}/anat", f"{new_r}/anat")
        new_f = f"{new_r}/func"
        print('new_f:', new_f)
        os.rename(root, new_f)

        if 'rest.nii.gz' in files:
            old_file = f"{new_f}/rest.nii.gz"
            print('old_file:', old_file)
            part = old_file.split('/')
            print('part:', part)
            new_file = f"{new_f}/{part[-4]}_{part[-3]}_task-rest_bold.nii.gz"
            print("new_file:", new_file)
            os.rename(old_file, new_file)

        old_af = f"{new_r}/anat/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
        new_af = f"{new_r}/anat/{part[-4]}_{part[-3]}_T1w.nii.gz"
        old_oldaf = f"{old_r}/anat/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
        print('old_af:', old_af)
        print('new_af:', new_af)
        print('old_oldaf:', old_oldaf)
        shutil.copyfile(old_af, new_af)