
# coding: utf-8

# In[ ]:


from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '192.168.43.238' )
myMessage = "Hello!"
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

mySocket.sendto(myMessage.encode('utf-8'),('192.168.43.238',5000))
   
while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    print (data)
sys.exit()

