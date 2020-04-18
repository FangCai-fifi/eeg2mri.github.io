import os
import sys
import shutil
from os import path

## This script can do well with IPCAS, IBATRT, JHNU, MRN_1 in CoRR.
## You may need to adjust the order of calling functions or even some of the functions when applying to other datasets

def batch_sub_num(dir, sub_n1, sub_n2):
# to change subject folder name from '002xxxx' to 'sub-002xxxx' under the root directory dir
# dir: str
#     root directory, containing all the subjects
# sub_n1: str
#     the smallest subject index
#     i.e. for folder name: JHNU_0025599_0025628, sub_n1 = '0025599'
# sub_n2: str
#     the largest subject index
#     i.e. for folder name: JHNU_0025599_0025628, sub_n2 = '0025628'

    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if (parts[-1] >= sub_n1 and parts[-1] <= sub_n2):
            new_r = "/".join(parts[:-1])
            # print('new_r:', new_r)
            new_d = f"{new_r}/sub-{parts[-1]}"
            # print('new_d:', new_d)
            os.rename(root, new_d)
    return

def batch_ses_num(dir, ses_n1='session_1', ses_n2='session_9'):
# to change session folder name from 'session_x' to 'ses-x'
# dir: str
#     root directory, containing all the subjects
# ses_n1: str
#     the smallest session index, default is 'session_1'
# ses_n2: str
#     the largest session index, default is 'session_9'

    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if (parts[-1] >= ses_n1 and parts[-1] <= ses_n2):
            new_r = "/".join(parts[:-1])
            # print('new_r:', new_r)
            num = parts[-1].split('_')[-1]
            # print('num:', num)
            new_d = f"{new_r}/ses-{num}"
            # print('new_d:', new_d)
            os.rename(root, new_d)
    return

def batch_anat(dir, anat_folder_name=['anat_1'], anat_file_name='anat.nii.gz'):
# to change anat folder name to 'anat' and T1 file name to 'sub-x_ses-y_T1w.nii.gz'
# dir: str
#     root directory, containing all the subjects
# anat_folder_name: list, default is ['anat_1']
# anat_file_name: str, default is 'anat.nii.gz'

    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if parts[-1] in anat_folder_name:
            new_r = "/".join(parts[:-1])
            # print('new_r:', new_r)
            new_d = f"{new_r}/anat"
            # print('new_d:', new_d)
            os.rename(root, new_d)
            
            if anat_file_name in files:
                old_f = f"{new_d}/{anat_file_name}"
                # print('old_f:', old_f)
                new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
                # print("new_f:", new_f)
                os.rename(old_f, new_f)
    return

def batch_dti(dir, dwi_folder_name=['dti_1'], dwi_name=['dti.bval','dti.bvec','dti.nii.gz']):
# to change dti folder name to 'dwi' and dti file names to 'sub-x_ses-y_dwi.(nii.gz/bval/bvec)'
# dir: str
#     root directory, containing all the subjects    
# dwi_folder_name: list, default is ['dti_1']
# dwi_name: list, default is ['dti.bval','dti.bvec','dti.nii.gz']
#     note: whatever the filename is, please keep it in order like ['x.bval','x.bvec','x.nii.gz']

    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if parts[-1] in dwi_folder_name:
            new_r = "/".join(parts[:-1])
            # print('new_r:', new_r)
            new_d = f"{new_r}/dwi"
            # print('new_d:', new_d)
            os.rename(root, new_d)
            
            for filename in files:
                if filename == dwi_name[0]:
                    old_f = f"{new_d}/{filename}"
                    # print('old_f:', old_f)
                    new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.bval"
                    # print("new_f:", new_f)
                    os.rename(old_f, new_f)
                if filename == dwi_name[1]:
                    old_f = f"{new_d}/{filename}"
                    # print('old_f:', old_f)
                    new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.bvec"
                    # print("new_f:", new_f)
                    os.rename(old_f, new_f)
                if filename == dwi_name[2]:
                    old_f = f"{new_d}/{filename}"
                    # print('old_f:', old_f)
                    new_f = f"{new_d}/{parts[-3]}_{parts[-2]}_dwi.nii.gz"
                    # print("new_f:", new_f)
                    os.rename(old_f, new_f) 
    return
    
def batch_rest(dir, rest_fname=['rest_1', 'rest_2'], rest_name='rest.nii.gz'):
# to rename rest folders and rest files  
# dir: str
#     root directory, containing all the subjects    
# rest_fname: list, default is ['rest_1','rest_2']
#     rest folder names
# rest_name: str, default is 'rest.nii.gz'
#     note: whatever the filename is, please keep it in order like ['x.bval','x.bvec','x.nii.gz']    
    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        # copy ses-x to ses_xy
        if (parts[-1] in rest_fname and parts[-1] == rest_fname[0]):
            part_num = parts[-1].split('_')[-1]
            # print('part_num:', part_num)
            old_r = "/".join(parts[:-1])
            # print('old_r:', old_r)
            new_r = "/".join(parts[:-1])
            # new_r = f"{new_r}/{parts[-2]}{part_num}"
            # print('new_r:', new_r)
            new_f = f"{old_r}/func"
            # print('new_f:', new_f)
            os.rename(root, new_f)
    
            if rest_name in files:
                old_file = f"{new_f}/{rest_name}"
                # print('old_file:', old_file)
                part = old_file.split('/')
                # print('part:', part)
                new_file = f"{new_f}/{part[-4]}_{part[-3]}_task-rest_bold.nii.gz"
                # print("new_file:", new_file)
                os.rename(old_file, new_file)
    
        if (parts[-1] in rest_fname and parts[-1] != rest_fname[0]):
            part_num = parts[-1].split('_')[-1]
            # print('part_num:', part_num)
            old_r = "/".join(parts[:-1])
            # print('old_r:', old_r)
            new_r = "/".join(parts[:-2])
            new_r = f"{new_r}/{parts[-2]}{part_num}"
            # print('new_r:', new_r)
            os.mkdir(new_r)
            shutil.copytree(f"{old_r}/anat", f"{new_r}/anat")
            new_f = f"{new_r}/func"
            # print('new_f:', new_f)
            os.rename(root, new_f)
    
            if rest_name in files:
                old_file = f"{new_f}/rest.nii.gz"
                # print('old_file:', old_file)
                part = old_file.split('/')
                # print('part:', part)
                new_file = f"{new_f}/{part[-4]}_{part[-3]}_task-rest_bold.nii.gz"
                # print("new_file:", new_file)
                os.rename(old_file, new_file)
    
            old_af = f"{new_r}/anat/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
            new_af = f"{new_r}/anat/{part[-4]}_{part[-3]}_T1w.nii.gz"
            old_oldaf = f"{old_r}/anat/{parts[-3]}_{parts[-2]}_T1w.nii.gz"
            # print('old_af:', old_af)
            # print('new_af:', new_af)
            # print('old_oldaf:', old_oldaf)
            shutil.copyfile(old_af, new_af)
            # shutil.copyfile(old_oldaf, new_af)
    return

def batch_rest_del(dir, ses_num_new=['ses-11','ses-12','ses-21','ses-22']):
# to delete the unnecessary file (a redundant 'T1w.nii.gz') in each new rest folders (ses-xy) created in batch_rest
# This is a special step when applying to IPCAS. May be needed when applying to similar original structures.
    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if (parts[-1] == 'anat' and parts[-2] in ses_num_new):
            # print('files:', files)
            file_num = len(files)
            for filename in files:
                part = filename.split('_')
                if part[-2] in ['ses-1', 'ses-2']:
                    del_file = f"{root}/{filename}"
                    # print('del_file:', del_file)
                    os.remove(del_file) 
    return  
  
def batch_empty_del(dir):
# to delete empty folders
    for root, dirs, files in os.walk(dir, topdown=True):
        # print('root:', root)
        # print('dirs:', dirs)
        # print('files:', files)
        parts = root.split('/')
        # print('parts:', parts)
        # print('parts[-1]:', parts[-1])
    
        if os.listdir(root) == []:
            print('deleted empty_root:', root)
            os.rmdir(root)
    return

def jhnu_batch_rest_add(dir):
# one more step when dealing with JHNU dataset in CoRR
    for root, dirs, files in os.walk(dir, topdown=True):
        print('root:', root)
        print('dirs:', dirs)
        print('files:', files)
        parts = root.split('/')
        print('parts:', parts)
        # print('parts[-1]:', parts[-1])

        if parts[-1] == 'ses-2':
            old_ar = "/".join(parts[:-1])
            old_ar = f"{old_ar}/ses-1/anat"
            new_ar = f"{root}/anat"
            os.mkdir(new_ar)
            old_af = f"{old_ar}/{parts[-2]}_ses-1_T1w.nii.gz"
            new_af = f"{root}/anat/{parts[-2]}_{parts[-1]}_T1w.nii.gz"
            shutil.copyfile(old_af, new_af)
    return

# root directory
dir = "/Users/fangcai/Downloads/data/MRN_0027010_0027048"

# batch_sub_num(dir, '0027010', '0027048')
# batch_ses_num(dir)
# batch_anat(dir)
# batch_dti(dir)
# batch_rest(dir)
# # batch_rest_del(dir) # use it on IPCAS datasets
# batch_empty_del(dir)

# jhnu_batch_rest_add(dir) # use it only on JHNU dataset

## to check each session folders
## some may miss necessary folders like 'anat'
for root, dirs, files in os.walk(dir, topdown=False):
    parts = root.split('/')
    if parts[-1] in ['ses-1','ses-2','ses-3']:
        print('root:', root)
        # if dirs != ['anat', 'func'] or files != ['anat', 'dwi', 'func']:
        print('folders:', dirs)