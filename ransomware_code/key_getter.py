import socket
from rsa import RSA
import os
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

#Generate these two primes somehow
sk, pk = RSA().Grsa(2048, 65537)
(n,e)=pk

message = bytes(str(pk), encoding='utf8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message)
    data = s.recv(1024)
    s.close()

y = int(str(data).replace("b", "").replace("'", ""))
key = RSA().Irsa(sk, y)
with open("key.txt", "w+") as file:
    file.write(str(key))