import cv2
import numpy as np

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)

while(True):
    # 從攝影機擷取一張影像
    ret, frame = cap.read()

    resize = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像
    blur = cv2.blur(gray,( 5 , 5 ) )
    canny = cv2.Canny(blur, 30 , 150)

    width = resize.shape[1] / 2
    height = resize.shape[0] / 2

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=5, maxRadius=300)

    # 繪圖
    img_circle = cv2.circle(resize, ((int)(width),(int)(height)), 2, (0,0,225), -1)

    # 顯示圖片
    cv2.imshow('resize', resize)
    #cv2.imshow('gray', gray)
    #cv2.imshow('blur', blur)
    cv2.imshow('canny', canny)

    # 若按下 q 鍵則離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
