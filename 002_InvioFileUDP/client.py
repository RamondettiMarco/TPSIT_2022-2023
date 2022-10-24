from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet



def valori_input_client():
    ip = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    username = input("Inserire il tuo username: ")
    
    return ip, porta, username

receiver = ("192.168.95.255", 5000)

def Client():
   
    buffer = f.read()
    #print(type(buffer))
    #print(buffer[:4096])
    
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("packet.py", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b'').to_bytes), receiver
            while True:
                #msg = input("Inserire il messaggio da inviare: ")
                #msg = f"l'utente {username.upper()} ha scritto: {msg}"
                msg = f.read(4096)
                if msg:
                    s.sendto(Packet(Packet.GO_ON, msg).to_bytes), receiver
            
if __name__ == "__main__":
    #ip, porta, username = valori_input_client()
    Client()