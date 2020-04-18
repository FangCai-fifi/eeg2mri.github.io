import os
import sys
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"
ses_num = ['session_1','session_2','session_3']

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts=root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1] in ses_num:
        new_r = "/".join(parts[:-1])
        print('new_r:', new_r)
        num = parts[-1].split('_')[-1]
        print('num:', num)
        new_d = f"{new_r}/ses-{num}"
        print('new_d:', new_d)
        os.rename(root, new_d)

