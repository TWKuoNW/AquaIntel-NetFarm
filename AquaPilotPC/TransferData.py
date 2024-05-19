import paramiko
import time

def sftp_transfer(remote_path, local_path, hostname, port, username, password):
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    sftp.close()
    transport.close()
    print('File transferred successfully.')

if __name__ == "__main__":
    remote_path = '/home/pi/AquaPilotFarm/sensor_data.txt'  # 替换为你在Raspberry Pi上的文件路径
    local_path = 'D:/智慧養殖專題/AquaIntel-NetFarm/AquaPilotPC/sensor_data.txt'  # 替换为你想在本地保存文件的路径
    hostname = '100.81.241.109'  # 替换为Raspberry Pi的IP地址
    port = 22  # SSH默认端口
    username = 'pi'  # 替换为你的Raspberry Pi用户名
    password = '123456'  # 替换为你的Raspberry Pi密码
    sftp_transfer(remote_path, local_path, hostname, port, username, password)
    """
    while True:
        sftp_transfer(remote_path, local_path, hostname, port, username, password)
        time.sleep(60)  # 每60秒检查并传输一次文件
    """