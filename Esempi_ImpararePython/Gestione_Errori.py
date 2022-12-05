#GESTIONE ERRORI
#ESEMPIO NUMERO DIVISO ZERO
#ESEMPIO METTO IN INPUT UNA STRINGA INVECE CHE UN NUMERO

def divisione(a, b):
    try:
        risultato = a / b
        print("il risultato della divisione è: " + str(risultato))
    except(ZeroDivisionError): #errore che viene visualizzato sul terminale se dividessi un numero per zero
        print("Hai effettuato una divisione per zero, causando un errore")

def moltiplicatore():
    try:
        a = int(input("inserisci il valore di a: "))
        b = int(input("inserisci il valore di b: "))
        risultato = a * b
        return risultato
    except(ValueError):
        print("Hey amico! solo caratteri numerici, grazie")
    finally:
        print("Fine del programma")

divisione(9, 3)

divisione(5, 0)

print(moltiplicatore())