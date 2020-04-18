import os
import sys
import shutil
from os import path

dir = "/Users/fangcai/Downloads/data/IBA_TRT_0027248_0027258"
c = 0

for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts = root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    if parts[-1] in ['ses-1', 'ses-2']:
        c = c + 1
        del_dir = root
        print('del_dir:', del_dir)
        shutil.rmtree(del_dir)

print(c)