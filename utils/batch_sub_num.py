import os
import sys
from os import path

dir = "/Users/fangcai/Downloads/data/IPCAS_7_0026104_0026119"
# sub_num = ['0026190','0026191','0026192','0026193','0026194','0026195','0026196','0026197','0026198','0026199',\
#            '0026200','0026201','0026202','0026203','0026204','0026205','0026206','0026207','0026208','0026209']
        #    '0025570','0025571','0025572','0025573','0025574','0025575','0025576','0025577','0025578','0025579',\
        #    '0025580','0025581','0025582','0025583']
#sub_num = ['0025498','0025499','0025500','0025501','0025502','0025503','0025504','0025505','0025506','0025507','0025508','0025509','0025510']
#sub_num = ['0025584','0025585']
dir_parts = dir.split('_')
for root, dirs, files in os.walk(dir, topdown=True):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    parts=root.split('/')
    print('parts:', parts)
    print('parts[-1]:', parts[-1])

    #if parts[-1] in sub_num:
    if (parts[-1] >= dir_parts[-2] and parts[-1] <= dir_parts[-1]):
        new_r = "/".join(parts[:-1])
        print('new_r:', new_r)
        new_d = f"{new_r}/sub-{parts[-1]}"
        print('new_d:', new_d)
        os.rename(root, new_d)