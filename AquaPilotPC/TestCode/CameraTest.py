# 測試opencv編解碼

import cv2
import numpy as np

image = cv2.imread('img/Logo1.png')
_, encoded_image = cv2.imencode('.jpg', image)
decoded_image = cv2.imdecode(np.frombuffer(encoded_image, np.uint8), cv2.IMREAD_COLOR)

cv2.imshow("123", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()