import sqlite3 as sql

def inserisciUtente(username, password):
    connection = sql.connect("utenti.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO UTENTI (Username,Password) VALUES (?,?)",(username,password)) #non si può usare fstring
    connection.commit()
    connection.close()
    
if __name__ == "__main__":
    username = input("Inserisci username:")
    password = input("Inserisci password:")
    inserisciUtente(username, password)