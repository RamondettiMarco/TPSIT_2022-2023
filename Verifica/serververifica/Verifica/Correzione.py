import sys
from socket import socket, AF_INET, SOCK_STREAM

BUFFER_SIZE = 4096

class Opzioni:
    def __init__(self, portaServer, host, porta):
        self.portaServer = int(portaServer)
        self.host = host
        self.porta = int(porta)
  
    def get_socket(self):
        return self.host, self.porta
 
def richiedi_dati(msg, sck):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sck)
        print("Connect")
        s.sendall(f"GET {msg}.json HTTP/1.0\n\n".encode("utf-8"))
        print("Request")
        data = s.recv(BUFFER_SIZE)
        print("Response")
        data = data + s.recv(BUFFER_SIZE)
        """dati = []
        data = True
        while data != None:
            data = s.recv(BUFFER_SIZE)
            if data != None:
                dati.append(data)
        dati = b''.join(dati)"""
    return data #dati
      
def main(args):
    opt = Opzioni(args[1], args[2], args[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", opt.portaServer))
        s.listen()
        while True:
            client, clientAddress = s.accept()
            data = client.recv(BUFFER_SIZE)
            #print(data)
            data = data.decode("utf-8")
            campi = data.split(" ")
            
            richiesta = richiedi_dati(campi[1], opt.get_socket())
            print(richiesta.decode("utf-8"))
            
            client.sendall(richiesta)
    
if __name__ == "__main__":
    main(sys.argv)