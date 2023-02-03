import requests
HOST = "http://192.168.1.123:5000"

def getPercorsi():
    percorsi = requests.get(HOST+"/api/v1/percorsi")
    return percorsi

def creaPercorso():
    new = input("inserire nuovo percorso: ")
    data = {"nome":new}
    requests.post(HOST+"/api/v1/percorsi", json=data)
    
def leggiPercorso(id):
    pass

def muoviPercorso(id):
    requests.get(f"{HOST}/api/v1/percorsi/{id}/muovi")
    
    
def main():
    operazione = "GO"
    while operazione != "ESCI":
        operazione = input("Inserire cosa fare -> (0: Leggi Tutti I Percorsi, 1: Leggi Singolo Percorso, 2: Crea Percorso, 3: Muovi Percorso, ESCI): ")
        if operazione == '0':  
            percorsi = getPercorsi()
            print(percorsi.content) 
        elif operazione == '1':
            percorso = leggiPercorso(int(input("Inserisci l'ID del percorso: ")))
            print(percorso.content)
        elif operazione == '2':
            creaPercorso()
        elif operazione == '3':
            muoviPercorso(int(input("Inserisci l'ID del percorso: ")))
    
if __name__ == '__main__':
    main()