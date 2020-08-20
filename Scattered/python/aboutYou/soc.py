import socket
import winreg
import datetime
import pyperclip
# import threading


class Socket(object):
    def __init__(self, client, server, path, port, cache, out_time, last_data, line_up):
        self.client = client
        self.server = server
        self.path = path
        self.port = port
        self.cache = cache
        self.out_time = out_time
        self.last_data = last_data
        self.line_up = line_up

    def send(self, var):
        try:
            if len(var) > 0:  # 如果粘贴板长度为0(空)，则抛出
                if var != self.last_data:  # 如粘贴板数据没有更新则抛出
                    self.last_data = var  # 更新粘贴板

                    client = socket.socket()
                    client.settimeout(self.out_time)
                    client.connect((self.client, self.port))
                    client.send(var.encode())
                    client.close()
                    print('发送成功！')
                print('未达发送条件！')
        except Exception as error:
            print('未发送任何数据，原因为：' + str(error))

    def get(self):
        try:
            server = socket.socket()
            server.settimeout(self.out_time)
            server.bind((self.server, self.port))
            server.listen(self.line_up)
            con, adr = server.accept()
            get_data = con.recv(self.cache).decode()
            pyperclip.copy(get_data)
            print('接收到的数据：' + '\n' + get_data + '\n已复制到粘贴板！')
            get_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '接收到了以下数据d：\n' + get_data + '\n'
            with open(self.path, mode='a') as f:
                f.write(get_data)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    p_server = socket.gethostbyname(socket.gethostname())  # 获取本机地址
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,  # 获取系统桌面地址
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    p_path = (winreg.QueryValueEx(key, "Desktop")[0])
    # 另一台电脑ip地址，本机ip地址，接收信息保存位置，监听端口，缓存，抛出时间，设置首次粘贴板记录为空，线程
    mySocket = Socket('192.168.100.7', p_server, p_path + '\\copy_data.txt', 6969, 2048, 2.5, None, 1)
    while True:
        mySocket.send(pyperclip.paste())
        mySocket.get()