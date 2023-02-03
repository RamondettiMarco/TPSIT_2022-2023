from socket import socket, AF_INET, SOCK_STREAM
from packet import Packet
from classeThread import ServerThread
BUFFER_SIZE = 1024


def valori_server():
    with open("confserver.txt", "r") as f:
        file = f.readlines()
        f.close()
    ip = file[0].strip() #toglie il \n
    porta = file[1]
    
    return ip, int(porta)

def chatServer(host, port):
    lista_msg = []
    lista_username = []
    receiver = (host, port)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(receiver)
        s.listen()
        #client, cliendAddresses = s.accept()
        while True:
            client, clientAddresses = s.accept()
            print(f"Connesso con {clientAddresses}")
            t = ServerThread(client, lista_msg, lista_username, clientAddresses, name="ThreadServer")
            t.start()
            
if __name__ == "__main__":
    host, porta = valori_server()
    chatServer(host, porta)