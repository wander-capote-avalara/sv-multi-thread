import socket 

host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 2000 
MESSAGE = b"Client B: ping"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != '':
    tcpClientB.send(MESSAGE)     
    data = tcpClientB.recv(BUFFER_SIZE)
    print(" Client B received data:", data)
    MESSAGE = b"Client B: ping:"

tcpClientB.close() 