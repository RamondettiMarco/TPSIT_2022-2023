import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    while True:
        msg = input("Inserisci un'operazione: ('exit' per uscire) ")
        client.sendall(msg.encode("utf-8"))
        if msg.lower() == "exit":
            client.close()
            break
        else:
            response = client.recv(4096).decode("utf-8")
            print(f"Risultato ricevuto: {response}")

if __name__ == "__main__":
    main()