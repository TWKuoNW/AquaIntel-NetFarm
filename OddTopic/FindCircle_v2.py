import cv2
import numpy as np

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)

while(True):
    # 從攝影機擷取一張影像
    ret, frame = cap.read()

    resize = cv2.resize(frame, (480, 360))

    hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
    # 定義顏色範圍
    lower_blue = np.array([0, 68, 255])  # 下限HSV值
    upper_blue = np.array([179, 189, 255])  # 上限HSV值
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blur = cv2.blur(mask,( 7 , 7 ) )
    canny = cv2.Canny(blur, 30 , 150)

    width = resize.shape[1] / 2
    height = resize.shape[0] / 2

    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=5, maxRadius=100)

    if circles is not None:
        print(type(circles))
        # 根據檢測到圓的信息，畫出每一個圓
        for circle in circles[0]:
            # 圓的基本信息
            print(circle[2])
            # 座標行列
            x = int(circle[0])
            y = int(circle[1])
            # 半徑
            r = int(circle[2])
            # 在原圖用指定顏色標記出圓的位置
            img = cv2.circle(resize, (x, y), r, (0, 0, 255), 3)
            img = cv2.circle(resize, (x, y), 2, (255, 255, 0), -1)

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
