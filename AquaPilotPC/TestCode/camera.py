# 測試相機是否正常運行(本地)
import cv2
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
   ret, frame = cap.read()
   cv2.imshow("frame", frame)
   key = cv2.waitKey(1)
   # ESC
   if key == 27:
      break
cap.release()
cv2.destroyAllWindows()
