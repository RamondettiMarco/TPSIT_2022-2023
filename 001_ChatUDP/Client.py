from socket import AF_INET, SOCK_DGRAM, socket

#PORT = 5000
#BROADCAST = "192.168.95.255"

def valori_input_client():
    ip = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    username = input("Inserire il tuo username: ")
    
    return ip, porta, username

def chatClient(ip, porta, username):
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("Inserire il messaggio da inviare: ")
            msg = f"l'utente {username.upper()} ha scritto: {msg}"
            msg = msg.encode('utf8')
            #s.sendto(msg, (BROADCAST, PORT))
            s.sendto(msg, (ip, porta))
            
if __name__ == "__main__":
    ip, porta, username = valori_input_client()
    chatClient(ip, porta, username)