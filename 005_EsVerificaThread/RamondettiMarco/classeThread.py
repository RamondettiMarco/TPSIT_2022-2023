import socket
import time
import threading

BUFFER_SIZE = 1024

class ServerThread(threading.Thread): #Ereditarietà
    def __init__(self, conn, lista_msg, lista_username, address, *args, **kwarg):
        threading.Thread.__init__(self, *args, **kwarg) #richiamo il costruttore della classe genitore (Thread)
        self.conn = conn
        self.lista_msg = lista_msg
        self.lista_username = lista_username
        self.address = address
    
    def run(self): #riscriviamo il metodo "run" della classe Thread -> OVERRIDE
        while True:
            comando = self.conn.recv(4096).decode("utf-8")
            print(f"Comando <<{comando}>> da {threading.current_thread().name}")
            res = b''
            if comando.lower() == "salva":
                msg = self.conn.recv(BUFFER_SIZE).decode("utf-8")
                msg = msg.split(";")
                self.lista_msg.append(msg[0]) #pkt.msg
                self.lista_username.append(msg[1]) #pkt.utente
                print(f"l'utente: << {msg[1]} >> ha scritto: << {msg[0]} >>") #pkt.utente pkt.msg
            elif comando.lower() == "leggi": #pkt.comando.lower()
                if len(self.lista_msg) < 1 or len(self.lista_username) < 1: #errore, non può leggere se non c'è niente
                    print("ERRORE! Niente da leggere")
                    error = "NON SONO PIU STATI INVIATI MESSAGGI"
                    res = error.encode('utf-8')
                else:
                    resend_msg = self.lista_msg.pop(0)
                    resend_username = self.lista_username.pop(0)
                    resend = f"il messaggio più vecchio è: << {resend_msg} >> scritto da: << {resend_username} >>"
                    res = resend.encode('utf-8')
            elif comando.lower() == "exit":
                res = f"Client {self.address} disconnesso".encode('utf-8')
            else:
                print("COMANDO INESISTENTE")
            self.conn.send(res)