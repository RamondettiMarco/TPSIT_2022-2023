import socket
import threading
import time

def server(connection, address):  
    print(f"Connesso con {address}")
    while connection:
        msg = connection.recv(4096).decode("utf-8")
        print(f"Operazione arrivata: {msg}")
        if msg.lower() == "exit":
            print("ERRORE")
            connection.close()
            break
        else:
            try:
                result = eval(msg)
                print(f"risultato operazione: {result}")
                connection.sendall(str(result).encode("utf-8"))
            except:
                connection.sendall("ERRORE! operazione fallita".encode("utf-8"))

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    while True:
        connection, address = s.accept()
        thread = threading.Thread(target=server, args=(connection, address))
        thread.start()
    
if __name__ == "__main__":
    main()