#stringhe e liste, similarità

s = "la pratica "
e = "rende perfetti"
print(s + e) #li stampa concatenati
print(s * 3) #stampa "s" 3 volte

a = [1, 2, "tre"]
b = [4, 5, "sei"]
print(a + b) #concatena anche la lista
print(a * 3) #stampa tre volte di fila anche la lista

print(len(s)) #len da la lunghezza della stringa
print(len(a)) #len da la lunghezza anche della lista, cioè quanti elementi ha

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = "qwerty"

print("q" in d) #restituisce True se c'è e False se non  c'è non
print(1 in c) #funziona sa con stringhe che con liste

def reverser(stringa):
    indice = (len(stringa)-1)
    nuovaStringa = ''
    while indice >= 0:
        nuovaStringa += stringa[indice]
        indice -= 1
    print(nuovaStringa)
    
stringa = 'abcdefg'
reverser(stringa)

stringa1 = "prova..."
print(stringa1[:-3]) #non stampa gli ultimi 3 elementi