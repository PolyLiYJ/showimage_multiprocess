import cv2
import time
import os
from PIL import Image
import sys

import matplotlib.image as mpimg # mpimg 用于读取图片
import matplotlib.pyplot as plt


def dispImgFullWin(image_start_index, image_end_index, interval, inputpath):
    for i in range(image_start_index, image_end_index,):
        imgname = inputpath + str(i)+'.bmp'
        img = cv2.imread(imgname)
        out_win = str(imgname)
        cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(out_win, 1280, 1024);
        cv2.moveWindow(out_win, 100, 0)
        #cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # full screen display
        cv2.imshow(out_win, img)
        print('begin show image ' + str(i) + " " + str(time.ctime(time.time())))
        cv2.waitKey(interval)
        print('close image'+ str(i) +" "+ str(time.ctime(time.time())))
        cv2.destroyAllWindows()


if __name__ =="__main__":
    inputpath = str(os.getcwd()) + "\\pictures\\project\\"
    N = 3
    image_start_index = 1
    image_end_index=4
    interval = 1000
    dispImgFullWin(image_start_index, image_end_index, interval, inputpath)
    # N = int(sys.argv[1])
    # interval = int(sys.argv[2])
    # path = sys.argv[3]

