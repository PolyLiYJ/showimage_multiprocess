import os
import cv2

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.bmp' or os.path.splitext(file)[1] == '.JPG' or os.path.splitext(file)[1] == '.JPEG' or os.path.splitext(file)[1] == '.jpeg'or os.path.splitext(file)[1] == '.png':
                fpath=os.path.join(root, file)
                L.append(fpath)
    return L

def main():
    for i in range(1,21):
        train_path = "data/calibration2/" + str(i) + "/"
        os.makedirs("data/calibration3/"+str(i))
        # files = file_name(train_path)
        for j in range(1, 39):
            file = train_path + str(j) +".bmp"
            print(file)
            img = cv2.imread(file)
            W = img.shape[1] #原图的宽
            H = img.shape[0] #原图的高
            print(W, H)
            W_R = int(H/3)   #需要裁剪的宽
            H_R = int(H/3)   #需要裁剪的高
            cropped = img [int(H/4):int(H*3/4),int(W/4):int(W*3/4)]
            cv2.imwrite("data/calibration3/"+str(i) +"/" + str(j)+".bmp", cropped)

if __name__ == "__main__":
    main()
