# Manual de Usuario

# Uso del ransomware

1. Descargue el codigo a la carpeta y cree dos pantallas de terminal. 
2. Haga source env/bin/activate o equivalente para activar el entorno de desarrollo.
3. Corra en un terminal python attacker_code/secret_server.py para activar el servidor de ataque
4. Corra python rware_code/key_getter.py para generar el secreto compartido (PASO 2 de la actividad)
5. Corra python rware_code/file_encrypter.py para encriptar los archivos y dejar la nota de ransom (PASO 3 de la actividad)
6. Corra python rware_code/payment_socket.py para notificar el atacante que ha pagado y recibir la llave de encriptacion simetrica x y la funcion para decriptar (PASO 4 de la actividad)
7. Guarde el archivo recibido por el punto 6 en rware_code y corralo para decriptar sus archivos (PASO 5 de la actividad) usando el x proveido
