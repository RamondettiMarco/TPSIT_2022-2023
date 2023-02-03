import socket
import time
import threading

class ServerThread(threading.Thread): #Ereditarietà
    def __init__(self, conn, *args, **kwarg):
        threading.Thread.__init__(self, *args, **kwarg) #richiamo il costruttore della classe genitore (Thread)
        self.conn = conn
    
    def run(self): #riscriviamo il metodo "run" della classe Thread -> OVERRIDE
        while True:
            ricevi = self.conn.recv(4096).decode("utf-8")
            print(f"{ricevi} da {threading.current_thread().name}")
            
            if ricevi.lower() == "exit":
                self.conn.close()
                break
            
            risp = input("Inserisci una risposta: ")
            self.conn.sendall(risp.encode("utf-8"))
            