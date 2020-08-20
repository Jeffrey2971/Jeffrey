import socket

# 设置socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置目的端口和IP
sendArr = ('www.jeffrey3261.vipgz1.idcfengye.com', 8000)
sendData = input('请输入你要发送的信息')
# 发送数据,此处有一个坑是sendto（）里面的参数必须二进制数据，不能直接传字符串
udpSocket.sendto(sendData.encode('utf-8'), sendArr)

udpSocket.close()