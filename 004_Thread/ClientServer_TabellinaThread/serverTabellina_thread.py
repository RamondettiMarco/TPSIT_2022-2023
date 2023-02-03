import socket
import threading
import time

def server(connection, address):  
    print(f"Connesso con {address}")
    while connection:
        msg = connection.recv(4096).decode("utf-8")
        print(f"Numero arrivato: {msg}")
        if msg.lower() == "exit":
            print("CHIUSURA")
            connection.close()
            break
        else:
            try:
                for i in range(11): #perché la tabellina ha da 0 a 10 operazioni
                    operazione = f"{msg}*{i}"
                    result = eval(operazione)
                    result = f"{msg}*{i} = {result}"
                    print(result)
                    connection.sendall(result.encode("utf-8"))
            except:
                print("ERRORE")
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