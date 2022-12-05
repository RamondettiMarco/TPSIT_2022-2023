import socket as sck

IP_ADDRESS = "127.0.0.1"    
PORT = 1984

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    testo = input()
    if(testo == "stop"):
        break

    s.sendto(testo.encode(), (IP_ADDRESS, PORT))

    data, addr = s.recvfrom(4096)
    print(data.decode())

s.close()