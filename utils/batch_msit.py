import os
import sys
from os import path

dir = "/Users/fangcai/Downloads/data/IBA_TRT_0027248_0027258"
msit_num = ['msit_1', 'msit_2', 'msit_3']
file_num = ['behavior.txt', 'logfile.txt', 'msit.nii.gz']

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts=root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1] in msit_num:
        if (files != []):
            path_d0 = f"{root}/{file_num[0]}"
            print('path_d0:', path_d0)
            path_d1 = f"{root}/{file_num[1]}"
            print('path_d1:', path_d1)
            path_d2 = f"{root}/{file_num[2]}"
            print('path_d2:', path_d2)
            path_df = root
            print('path_df:', path_df)
            os.remove(path_d0)
            os.remove(path_d1)
            os.remove(path_d2)
            os.removedirs(path_df)