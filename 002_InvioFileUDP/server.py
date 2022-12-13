from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet
#from distutils.file_util import write_file
#from pathlib import Path

MAX_SIZE = 7000

def valori_input_server():
    host = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    
    return host, porta

def write_file(buffer):
    with open("result.pdf", "wb") as f:
        f.write(buffer)

def Server():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', 5000))
        file = []
        
        while True:
            msg = s.recvfrom(MAX_SIZE)
            packet = Packet.from_bytes(msg[0])
            if packet.status == Packet.NEW_FILE:
                file = []
            elif packet.data and len(packet.data) > 0:
                file.append(packet.data)
            elif packet.status == Packet.END_FILE:
                file_completo = b''.join(file)
                #path = Path('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python').joinpath('002_InvioFileUDP/results.pdf')
                #path.write_file(file_completo)
                write_file(file_completo)


if __name__ == "__main__":
    #host, porta = valori_input_server()
    Server()