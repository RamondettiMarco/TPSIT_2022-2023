import socket
import threading
import time

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    while True:
        connection, address = server.accept()
        print(f"Connesso con {address}")
        msg = connection.recv(4096).decode("utf-8")
        result = eval(msg) # ! pericoloso, mai usare in un programma -> molto potente, può eseguire qualsiasi script in "msg"
        #eval esegue una stringa ricevuta, se ci sono dei comandi funzionanti dentro
        print(result)
        time.sleep(2)
        connection.sendall("Messaggio ricevuto".encode("utf-8"))
    
if __name__ == "__main__":
    main()