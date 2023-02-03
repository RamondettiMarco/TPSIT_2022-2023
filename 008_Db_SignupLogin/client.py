from socket import AF_INET, SOCK_STREAM, socket

BUFFER_SIZE = 1024

def valori_input_client():
    ip = input("Inserire l'indirizzo IP: ")
    porta = int(input("Inserire la porta: "))
    
    return ip, porta

def main(ip, porta):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((ip, porta))
        while True:
            msg = False
            while msg == False:
                comando = input("inserisci il comando (signup - login - exit): ")
                if comando.lower() != "login" and comando.lower() != "signup" and comando.lower() != "exit":
                    print("COMANDO NON VALIDO")
                else:
                    msg = True
            if comando.lower() == "exit":
                messaggio = f"{comando};username;password"
                messaggio = messaggio.encode('utf-8')
                s.sendto(messaggio, (ip, porta))
                break
            controllo = True
            while controllo == True:
                username = input("Inserisci username (; non valido): ")
                password = input("Inserisci password (; non valido): ") 
                if ';' in username:
                    print("USERNAME NON VALIDO")
                if ';' in password:
                    print("PASSWORD NON VALIDA")
                if ';' not in password and ';' not in username:
                    controllo = False
            messaggio = f"{comando};{username};{password}"
            messaggio = messaggio.encode('utf-8')
            s.sendto(messaggio, (ip, porta))
            result = s.recv(BUFFER_SIZE)
            print(result.decode('utf-8'))
            if result.decode('utf-8') == "LOGIN SUCCESSFUL":
                name = input("Inserisci la ricerca dell'username: ")
                s.send(name.encode('utf-8'))
                
                user = s.recv(BUFFER_SIZE)
                print(f"Username ricercati: {user.decode('utf-8')}")
            
if __name__ == "__main__":
    ip, porta = valori_input_client()
    main(ip, porta)