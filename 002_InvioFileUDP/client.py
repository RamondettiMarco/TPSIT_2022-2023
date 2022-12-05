from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet



def valori_input_client():
    ip = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    #username = input("Inserire il tuo username: ")
    
    return ip, porta #, username

receiver = ("127.0.0.1", 5000)

def Client():
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("RamondettiMarco_TipologiaC.pdf", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b'').to_bytes(), receiver)
            data = True
            while data:
                data = f.read(4096)
                if data:
                    s.sendto(Packet(Packet.GO_ON, data).to_bytes(), receiver)
                    #time.sleep(0.001)

            s.sendto(Packet(Packet.END_FILE, b'').to_bytes(), receiver)
            
if __name__ == "__main__":
    #ip, porta, username = valori_input_client()
    Client()