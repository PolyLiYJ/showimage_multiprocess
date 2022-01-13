import cv2
import time
import sys
import os
import keyboard


def takephoto(image_start_index, image_end_index, interval, outputpath):

    # 0 is computer camera, 1 is USB camera
    # while keyboard.read_key() != "q":
    #     with open('index.txt', 'rt') as f:
    #         index_new = int(f.read())
    #     if index_new > index:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    for index in range(image_start_index, image_end_index):
        # give some time to display the image
        print("capture image" + str(index) +" " + str(time.ctime(time.time())))
        ret, frame = cap.read()
        print("end capture" + str(index) +" " + str(time.ctime(time.time())))
        resize = cv2.resize(frame, (1280, 1024), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(outputpath +'/'+ str(index)+'.bmp', resize)
        time.sleep(float(interval)/1000)
    cap.release()
    return 0

if __name__=='__main__':
    # N = int(sys.argv[1])
    # interval = float(sys.argv[2])/1000
    # outputpath = sys.argv[3]

    N = 3
    image_start_index = 1
    image_end_index = 4
    interval = 1000
    Path = 'pictures/model/'
    print('Begin to take pictures..........')
    takephoto(image_start_index, image_end_index, interval, Path)
    image_start_index = 4
    image_end_index = 7
    takephoto(image_start_index, image_end_index, interval, Path)
    print('Finished !!')

