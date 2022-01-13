
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import os
from Project import dispImgFullWin
from CaptureImage import takephoto
import sys

class Thread1(threading.Thread):
    def __init__(self, image_start_index, image_end_index, interval, inputpath):
        threading.Thread.__init__(self)
        self.image_start_index = image_start_index
        self.image_end_index = image_end_index
        self.interval = interval
        self.inputpath = inputpath

    def run(self):
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
       # threadLock.acquire()
        dispImgFullWin(self.image_start_index, self.image_end_index, self.interval, self.inputpath)
        # 释放锁
       # threadLock.release()

class Thread2(threading.Thread):
    def __init__(self, image_start_index, image_end_index, interval, outputpath):
        threading.Thread.__init__(self)
        self.image_start_index = image_start_index
        self.image_end_index = image_end_index
        self.interval = interval
        self.outputpath = outputpath

    def run(self):
        takephoto(self.image_start_index, self.image_end_index, self.interval, self.outputpath)

def multi_process(image_start_index, image_end_index, interval, inputpath, outputpath):
    # 创建新线程
    thread1 = Thread1(image_start_index, image_end_index, interval, inputpath)
    thread2 = Thread2(image_start_index, image_end_index, interval, outputpath)

    # 开启新线程
    thread1.start()
    time.sleep(interval/1000/2)
    thread2.start()

    threads = []
    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    #
    #等待所有线程完成
    for t in threads:
        t.join()

    print("Capture image " + str(image_start_index) + " to " + str(image_end_index-1) )
    print("Exiting Main Thread")

if __name__=='__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    interval = int(sys.argv[3])
    inputpath = sys.argv[4]
    outputpath = sys.argv[5]
    multi_process(start, end, interval, inputpath, outputpath)
    # inputpath = str(os.getcwd()) + "\\pictures\\project\\"
    # outputpath = str(os.getcwd()) + "\\pictures\\model\\"
    # N = 15
    # interval = 2000
    # batch = 15
    # inputpath = str(os.getcwd()) + "\\pictures\\project\\"
    # outputpath = str(os.getcwd()) + "\\pictures\\model\\"
    # ## clear the outputpath
    # f = os.walk(outputpath)
    # for path, dir_list, file_list in f:
    #     for file_name in file_list:
    #         os.remove(os.path.join(path, file_name))
    # ## display by batch
    # for i in range(0, int(N / batch) + 1):
    #     if i < int(N / batch):
    #         image_start_index = i * batch + 1
    #         image_end_index = (i + 1) * batch + 1  # [i*5+1, (i+1)*5]
    #     else:
    #         image_start_index = i * batch + 1
    #         image_end_index = N + 1
    #     multi_process(image_start_index, image_end_index, interval, inputpath, outputpath)