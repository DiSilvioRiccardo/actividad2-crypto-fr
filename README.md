# Manual de Usuario

# Uso del ransomware

1. Descargue el codigo a la carpeta y cree dos pantallas de terminal. 
2. Haga source env/bin/activate o equivalente para activar el entorno de desarrollo.
3. Corra en un terminal cd attacker_code y luego python secret_server.py para activar el servidor de ataque
4. Haga cd .. luego cd rware_code y corra python key_getter.py para generar el secreto compartido (PASO 2 de la actividad)
5. Corra python file_encrypter.py para encriptar los archivos y dejar la nota de ransom (PASO 3 de la actividad)
6. Corra python payment_socket.py para notificar el atacante que ha pagado y recibir la llave de encriptacion simetrica x y la funcion para decriptar (PASO 4 de la actividad)
7. Guarde el archivo recibido por el punto 6 en rware_code y corralo para decriptar sus archivos (PASO 5 de la actividad) usando el x proveido
