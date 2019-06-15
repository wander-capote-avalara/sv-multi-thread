import socket 
from threading import Thread 
import socketserver

class ClientThread(Thread): 
 
    def __init__(self,ip,port,conn): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        print(f"New server socket thread started for {ip}:{port}")
 
    def run(self): 
        while True : 
            data = self.conn.recv(1024) 
            print("Server received data:", data)
            MESSAGE = b"pong"
            if not data:
                print("Connection finished")
                break
            self.conn.send(MESSAGE)

TCP_IP = '127.0.0.1' 
TCP_PORT = 12345 
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind((TCP_IP, TCP_PORT)) 
threads = [] 
server.listen() 

while True: 
    print("Multithreaded server : Waiting for connections from clients...")
    (conn, (ip,port)) = server.accept() 
    newthread = ClientThread(ip,port,conn) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 