import cv2

stream_url = 'http://192.168.0.101:8080/video'

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("無法接收幀，退出...")
        break
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
