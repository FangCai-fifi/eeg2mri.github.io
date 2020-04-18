import os
import sys
import shutil
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts = root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    # copy ses-x to ses_xy
    if os.listdir(root) == []:
        print('empty_root:', root)
        os.rmdir(root)