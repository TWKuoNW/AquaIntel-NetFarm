import cv2
import numpy as np

# 定義空回傳
def nothing(x):
    pass

# 創建黑色畫布
cv2.namedWindow('Color Filter')

# 新增滑動模塊
cv2.createTrackbar('Hue Min', 'Color Filter', 0, 179, nothing)
cv2.createTrackbar('Hue Max', 'Color Filter', 179, 179, nothing)
cv2.createTrackbar('Saturation Min', 'Color Filter', 0, 255, nothing)
cv2.createTrackbar('Saturation Max', 'Color Filter', 255, 255, nothing)
cv2.createTrackbar('Value Min', 'Color Filter', 0, 255, nothing)
cv2.createTrackbar('Value Max', 'Color Filter', 255, 255, nothing)

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)

while True:
    # 從攝影機擷取一張影像
    ret, frame = cap.read()
    resize = cv2.resize(frame, (480, 360))

    # 取值
    hue_min = cv2.getTrackbarPos('Hue Min', 'Color Filter')
    hue_max = cv2.getTrackbarPos('Hue Max', 'Color Filter')
    sat_min = cv2.getTrackbarPos('Saturation Min', 'Color Filter')
    sat_max = cv2.getTrackbarPos('Saturation Max', 'Color Filter')
    val_min = cv2.getTrackbarPos('Value Min', 'Color Filter')
    val_max = cv2.getTrackbarPos('Value Max', 'Color Filter')

    # BGR to HSV
    hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

    # 定義顏色區間
    lower_bound = np.array([hue_min, sat_min, val_min])
    upper_bound = np.array([hue_max, sat_max, val_max])

    # 過濾
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(resize, resize, mask=mask)

    # show
    cv2.imshow('Color Filter', result)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
