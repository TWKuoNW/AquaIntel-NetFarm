import socket
import cv2
import numpy as np

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.0.101', 6789)
message = 'Hello, UDP server!'
client_socket.sendto(message.encode(), server_address)

while(True):
    data, address = client_socket.recvfrom(65500)

    decoded_image = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
    
    cv2.imshow("123", decoded_image)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
client_socket.close()