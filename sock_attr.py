"""
套接字属性
"""

from socket import *

s = socket()

# 端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

s.bind('127.0.0.1',8888)
s.listen(3)



c,addr = s.accept()
print(c.getpeername())
c.recv(1024)