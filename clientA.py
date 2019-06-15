import socket 

host = '127.0.0.1' 
port = 12345
BUFFER_SIZE = 2000 
MESSAGE = b"Client A: ping:"
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != '':
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print(" Client A received data:", data)
    MESSAGE = b"Client A: ping:"

tcpClientA.close() 