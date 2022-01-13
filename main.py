# !/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import os
from Project import dispImgFullWin
from CaptureImage import takephoto
from multiprocess import  multi_process

if __name__=='__main__':
    N = 36
    interval = 2000
    batch = 10
    inputpath = str(os.getcwd()) + "\\pictures\\project\\"
    outputpath = str(os.getcwd()) + "\\pictures\\model\\"
    ## clear the outputpath
    f = os.walk(outputpath)
    for path, dir_list, file_list in f:
        for file_name in file_list:
            os.remove(os.path.join(path, file_name))
    ## display by batch
    for i in range(0, int(N / batch) + 1):
        if i < int(N / batch):
            image_start_index = i * batch + 1
            image_end_index = (i + 1) * batch + 1  # [i*5+1, (i+1)*5]
        else:
            image_start_index = i * batch + 1
            image_end_index = N + 1
        cmd = "python multiprocess.py " + " " + str(image_start_index) + " " + str(image_end_index) + " " + str(interval) + " " + str(inputpath) + " " + str(outputpath)
        print(cmd)
        os.system(cmd)