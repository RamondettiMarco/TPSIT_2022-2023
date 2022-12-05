#Trasformate il programma in una funzione mysqrt() che prenda come argomento un numero e restituisca la sua radice,
#provocando un ValueError se il suo argomento è negativo. Dovete eliminare, nella funzione,
#tutte le istruzioni che stampano i risultati intermedi e trasformare l'ultima istruzione 
#(che stampa la radice in una return. Scrivete poi due istruzioni che chiamino tale funzione,
#una con un numero positivo ed una con un numero negativo come argomento.
from math import sqrt

def mysqrt(a):
    try:
        risultato = sqrt(a)
    except ValueError:
        risultato = "Argomento negativo, Errore"
    return risultato

print(mysqrt(25))
print(mysqrt(-25))