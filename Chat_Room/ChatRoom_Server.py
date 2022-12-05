import socket
import threading
import csv

def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Nome", "Indirizzo", "Porta", "Messaggio Client")
        writer.writerow(header)
        f.close()

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)
        f.close()

data_file = "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Chat_Room\\chat.csv"
create_csv_file(data_file)

PORT = 5000 
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.88.71"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
PASSWORD = "raspberry"

clients, names = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def startChat():
   
    print("SERVER is working on: " + SERVER)
    server.listen()
     
    while True:
        conn, addr =  server.accept()
        conn.send("NAME".encode(FORMAT))

        name = conn.recv(1024).decode(FORMAT)
        names.append(name)
        clients.append(conn)      
        print(f"Name is :{name}")
        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))       
        conn.send('Connection successful!'.encode(FORMAT))

        thread = threading.Thread(target = handle, args = (conn, addr, name))
        thread.start()

        print(f"active connections {threading.activeCount()-1}")
        

def handle(conn, addr, name):
   
    print(f"new connection {addr}")
    connected = True
     
    while connected:
        message = conn.recv(1024)
        data = (name, addr[0], addr[1], message.decode())
        add_csv_data(data_file, data)
        broadcastMessage(message)

    conn.close()

def broadcastMessage(message):
    for client in clients:
        client.send(message)

startChat()