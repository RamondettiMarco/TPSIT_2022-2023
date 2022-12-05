from socket import socket, AF_INET, SOCK_STREAM
MAX_SIZE = 4096

def dati_input():
    indirizzo_sock = input("Inserisci l'indirizzo del socket (127.0.0.1): ")
    porta_sock = int(input("Inserisci la porta del socket (8000): "))
    sock = (indirizzo_sock, porta_sock)
    porta = int(input("Inserisci la porta: "))
    return sock, porta


def modifica_messaggio(richiesta_http):
    richiesta_splittata = richiesta_http.decode('utf-8').split(" ") #richiesta splittata, ho tutte le singole informazioni 
    msg = richiesta_splittata[1] # ho solo la richiesta da inviare al server, es. /data
    help = controlla_help(msg)
    if help == True:
        msg_finale = "/dati"+"\n"+"/divina"
    else:
        msg_completo = msg + ".json" #ora posso inviarlo al server
        msg_finale = "GET "+msg_completo+" HTTP/1.1"+"\n\n"
        msg_finale = msg_finale.encode("utf-8") 
    
    return msg_finale   

def controlla_help(msg):
    if msg == "/help":
        help = True
    else:
        help = False
    return help

def ricezione(receiver):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(receiver)

        s.listen()
        print("In Ascolto")

        client, clientAddress = s.accept()
        print(f"Si è connesso: {clientAddress[0]} con successo alla porta {clientAddress[1]}")
        
        richiesta_http = s.recv(MAX_SIZE) # tutta la richiesta
        richiesta_http = richiesta_http + s.recv(MAX_SIZE)
        msg_completo = modifica_messaggio(richiesta_http) # solo ciò che devo reinviare, es. GET /data.json HTTP/1.1
        
        client.sendall(msg_completo)
        
        return msg_completo
    
def invio_richiesta(sock, msg_completo):
    with socket(AF_INET, SOCK_STREAM) as sck:
        sck.connect(sock)
    
        sck.sendall(msg_completo)
        
        ritorno_richiesta = sck.recv(MAX_SIZE)
        print(ritorno_richiesta)
        
    return ritorno_richiesta

def run_server(sock, porta):
    receiver = ("0.0.0.0", porta)
    
    msg_completo = ricezione(receiver) 
    print(msg_completo)
    
    str_help = "/dati"+"\n"+"/divina"
    
    #ritorno_richiesta = invio_richiesta(sock, msg_completo)
    #invio_richiesta(receiver, ritorno_richiesta)
    
    if msg_completo != str_help:
        ritorno_richiesta = invio_richiesta(sock, msg_completo)
        invio_richiesta(receiver, ritorno_richiesta)
    else:
        print("richiesta help: " + msg_completo)
    
        

if __name__ == "__main__":
    sock, porta = dati_input()
    run_server(sock, porta)