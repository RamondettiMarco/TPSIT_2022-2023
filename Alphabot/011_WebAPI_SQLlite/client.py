import requests
HOST = "http://localhost:5000"

def getPercorsi():
    percorsi = requests.get(HOST+"/api/v1/percorsi")
    return percorsi

def creaPercorso():
    new = input("inserire nuovo percorso: ")
    data = {"nome":new}
    requests.post(HOST+"/api/v1/percorsi", json=data)
    
def main():
    creaPercorso()
    percorsi = getPercorsi()
    print(percorsi.content) 

if __name__ == '__main__':
    main()