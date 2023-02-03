from socket import AF_INET, SOCK_STREAM, socket

BUFFER_SIZE = 1024

def valori_client():
    with open("confclient.txt", "r") as f:
        file = f.readlines()
        f.close()
    username = input("Inserire il tuo username: ")
    ip = file[0].strip() #toglie \n
    porta = file[1]
    
    return ip, int(porta), username

def costruisciMessaggio(username):
    msg = input("Inserire il messaggio da inviare: ")
    msg_completo = f"{msg};{username}"
    msg_completo = msg_completo.encode('utf8')
    return msg_completo

def controllaComando(comando, s):
    res = ""
    if comando.lower() == "leggi":
        lettura = s.recv(BUFFER_SIZE)
        res = lettura.decode("utf-8")
    elif comando.lower() == "salva":
        msg_completo = costruisciMessaggio(username)
        res = "Salvo il messaggio inviato"
        s.send(msg_completo)
    elif comando.lower() == "exit":
        res = "Chiudo connessione"
        s.close()
    else:
        res = "COMANDO INESISTENTE"
    return res

def chatClient(ip, porta, username):
    client = (ip, porta)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(client)
        while True:
            comando = input("Inserire il comando da inviare: ")
            s.send(comando.encode("utf-8"))
            result = controllaComando(comando, s)
            print(result)           
            if result == "Chiudo connessione":
                break
            
            
if __name__ == "__main__":
    ip, porta, username = valori_client()
    chatClient(ip, porta, username)