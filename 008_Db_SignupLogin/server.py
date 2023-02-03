import sqlite3 as sql
from socket import socket, AF_INET, SOCK_STREAM

BUFFER_SIZE = 1024

def valori_input_server():
    host = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    
    return host, porta

def logIn(username, password, connection):
    result = ""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UTENTI WHERE (Username = ? AND Password = ?)",(username,password)) #non si può usare fstring
    if len(cursor.fetchall()) >= 1:
        result = "LOGIN SUCCESSFUL"
    else:
        result = "LOGIN FAIL"
    connection.commit()
      
    return result
    
def signUp(username, password, connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO UTENTI (Username,Password) VALUES (?,?)",(username,password)) #non si può usare fstring
    connection.commit()
    
    return f"Nuovo utente -> {username}"
    
def ricercaUtente(name, connection):
    cursor = connection.cursor()
    username = cursor.execute('SELECT Username FROM UTENTI')
    users = cursor.fetchall()
    cursor.execute('''SELECT Username FROM UTENTI WHERE (%s) LIKE ?'''%users,(name,)) #non si può usare fstring
    for row in cursor.fetchall():
        print(row)
    connection.commit()
    
    return cursor.fetchall()

def main(host, porta):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, porta))
        s.listen()
        print("Server in ascolto...\n")
        connection = sql.connect("utenti.db")
        while True:
            client, address = s.accept()
            print(f"Si è connesso: {address[0]} con successo alla porta {address[1]}")
            
            messaggio = client.recvfrom(BUFFER_SIZE)
            msg = messaggio[0].decode("utf-8").split(";")
            comando = msg[0]
            username = msg[1]
            password = msg[2]
            if comando.lower() == "login":
                result = logIn(username, password, connection)
                print(result)
                client.sendall(result.encode("utf-8"))
                if result == "LOGIN SUCCESSFUL":
                    name = client.recvfrom(BUFFER_SIZE)
                    print(f"Ricerca di -> {name[0].decode('utf-8')}")
                    usr = ricercaUtente(name[0].decode("utf-8"), connection)
                    print(usr)
                    client.sendall(usr.encode("utf-8"))
            elif comando.lower() == "signup":
                ret = signUp(username, password, connection)
                print(ret)
                client.sendall(ret.encode('utf-8'))
            elif comando.lower() == "exit":
                connection.close()
                break

if __name__ == "__main__":
    host, porta = valori_input_server()
    main(host, porta)