import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

def decrypt(key, filename):
	chunksize = 64*1024
	outputFile = filename[:-4]+'d'

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor= AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize)


def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

def decryptFiles(x, files):
    os.chdir("./important_files")
    for file in files:
        decrypt(getKey(x), file)

    