from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet

BUFFER_SIZE = 4096

def valori_input_client():
    ip = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    file = input("Inserire il tuo file: ")
    
    return ip, porta, file

receiver = ("127.0.0.1", 5000)

def Client():
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("RamondettiMarco_TipologiaC.pdf", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b'').to_bytes(), receiver)
            data = True
            while data:
                data = f.read(BUFFER_SIZE)
                if data:
                    s.sendto(Packet(Packet.GO_ON, data).to_bytes(), receiver)
                    #time.sleep(0.001)

            s.sendto(Packet(Packet.END_FILE, b'').to_bytes(), receiver)
            
if __name__ == "__main__":
    #ip, porta, file = valori_input_client()
    Client()