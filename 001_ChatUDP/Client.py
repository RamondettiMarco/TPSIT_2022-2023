from socket import AF_INET, SOCK_DGRAM, socket

#PORT = 5000
#BROADCAST = "192.168.95.255"

def chatClient():
    ip = input("Inserire l'indirizzo IP: ")
    porta = input("Inserire la porta: ")
    username = input("Inserire il tuo username: ")
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("Inserire il messaggio da inviare: ")
            msg = f"l'utente {username.upper()} ha scritto: {msg}"
            msg = msg.encode('utf8')
            #s.sendto(msg, (BROADCAST, PORT))
            s.sendto(msg, (ip, int(porta)))
            

if __name__ == "__main__":
    chatClient()