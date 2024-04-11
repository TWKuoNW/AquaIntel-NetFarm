import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 9999

server_socket.bind((host, port))
server_socket.listen(5)

try:
    while True:
        print("等待客戶端連線...")
        client_socket, addr = server_socket.accept()

        print(f"連線地址: {str(addr)}")
        msg = '連線成功！' + "\r\n"
        client_socket.send(msg.encode('utf-8'))
        client_socket.close()
except KeyboardInterrupt:
    print("準備關閉伺服器...")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    server_socket.close()
    print("伺服器關閉。")
