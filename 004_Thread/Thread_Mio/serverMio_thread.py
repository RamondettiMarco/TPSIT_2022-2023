import socket
import threading
import time
from classe import ServerThread


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    while True:
        connection, address = server.accept()
        print(f"Connesso con {address}")
        
        nome = input("Inserisci nome: ")
        t = ServerThread(connection, name="Thread_Msg")       
        t.start()
    
if __name__ == "__main__":
    main()