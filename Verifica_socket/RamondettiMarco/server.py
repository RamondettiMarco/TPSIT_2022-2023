from socket import socket, AF_INET, SOCK_STREAM
from packet import Packet

BUFFER_SIZE = 1024


def valori_server():
    with open("confserver.txt", "r") as f:
        file = f.readlines()
        f.close()
    ip = file[0].strip() #toglie il \n
    porta = file[1]
    
    return ip, int(porta)

def controllaComando(comando, client, lista_msg, lista_username):
    res = b''
    if comando.lower() == "salva":
        msg = client.recv(BUFFER_SIZE)
        #pkt = Packet.decoding(msg)
        msg = msg.decode("utf-8")
        msg = msg.split(";")
        lista_msg.append(msg[0]) #pkt.msg
        lista_username.append(msg[1]) #pkt.utente
        print(f"l'utente: << {msg[1]} >> ha scritto: << {msg[0]} >>") #pkt.utente pkt.msg
    elif comando.lower() == "leggi": #pkt.comando.lower()
        if len(lista_msg) < 1 or len(lista_username) < 1: #errore, non può leggere se non c'è niente
            error = "NON SONO PIU STATI INVIATI MESSAGGI"
            res = error.encode('utf-8')
        else:
            resend_msg = lista_msg.pop(0)
            resend_username = lista_username.pop(0)
            resend = f"il messaggio più vecchio è: << {resend_msg} >> scritto da: << {resend_username} >>"
            res = resend.encode('utf-8')
    return res

def chatServer(host, port):
    lista_msg = []
    lista_username = []
    receiver = (host, port)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(receiver)
        s.listen()
        #client, cliendAddresses = s.accept()
        while True:
            client, cliendAddresses = s.accept()
            comando = client.recv(BUFFER_SIZE)
            comando = comando.decode("utf-8")
            resend = controllaComando(comando, client, lista_msg, lista_username)
            client.send(resend)
          
            
if __name__ == "__main__":
    host, porta = valori_server()
    chatServer(host, porta)