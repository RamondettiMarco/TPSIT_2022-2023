import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    while True:
        msg = input("Inserisci un numero di cui fare la tabellina: ('exit' per uscire) ")
        client.sendall(msg.encode("utf-8"))
        if msg.lower() == "exit": # se scrivo exit esco
            client.close()
            break
        else:
            operazione = 0
            while operazione != "ERRORE" and operazione != "FINITO": #se ho inserito un input sbagliato o ho finito l atabellina esco
                response = client.recv(4096).decode("utf-8")
                print(f"Risultato {operazione} ricevuto: {response}")
                if response[:6] != "ERRORE": # se non ho ricevuto errore, quindi ho inserito correttamente l'input
                    if operazione >= 10: #perché la tabellina ha da 0 a 10 operazioni
                        operazione = "FINITO" #ho finito la tabellina
                    else:
                        operazione+=1 #continuo la tabellina
                else:
                    operazione = "ERRORE" # ho sbagliato a scrivere l'input

if __name__ == "__main__":
    main()