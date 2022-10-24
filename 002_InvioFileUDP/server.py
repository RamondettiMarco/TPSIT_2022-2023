from socket import socket, AF_INET, SOCK_DGRAM
from packet import Packet
from distutils.file_util import write_file

BUFFER_SIZE = 1024

def valori_input_server():
    host = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    
    return host, porta

def Server():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))
        file = []
        while True:
            msg, address = s.recvfrom(BUFFER_SIZE)
            packet = Packet.from_bytes(msg) 
            if packet.status == Packet.NEW_FILE:
                file = []
            if packet.data and len(packet.data) > 0:
                file.append(packet.data)
            if packet.status == Packet.END_FILE:
                write_file(b''.join(file))
            #msg.decode('utf-8')
            #print(f"L'username: {msg[1]} ha scritto il messaggio: {msg[0]}")
if __name__ == "__main__":
    #host, porta = valori_input_server()
    Server()