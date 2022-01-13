import cv2

# 调用usb摄像头
camera_id = 0; # 0 is computer camera, 1 is USB1 camera
cap = cv2.VideoCapture(camera_id)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc("M", "J", "P", "G"))  # ?1为啥要重设

# 显示
while True:
    ret, frame = cap.read()
    cv2.imshow("window1", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 关闭
cap.release()
cv2.destroyAllWindows()
