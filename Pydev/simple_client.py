#!/usr/bin/env python
import socket

s = socket.socket()
host= socket.gethostname()
port=1357

s.connect((host,port))
print(s.recv(1024))
 #simple server code below
# s=socket.socket()
 #host=socket.gethostname()
 #port=1357
 #s.bind((host,port))

 #s.listen(5)
 #while True:
      #c,addr=s.accept()
      #print("Accepted the connection from :",addr)
      #c.send('Thanks for connecting')
      #c.close()
