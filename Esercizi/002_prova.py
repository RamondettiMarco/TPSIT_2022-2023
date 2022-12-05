cnt = 0
while cnt <= 10:
    print(cnt)
    cnt += 1 #cnt++ NON esiste

#se uso ciclo for piu' semplice
#numeri da 0 a 11 
for n in range(11):
    print(n)


#numeri da 3 a 11 a range for(i=3; i<=11, i+=2)
for numero in range(3, 11, 2):
    print(numero)

#numeri al contrario da 10 a 0, uso il - per andare indietro
for n in range(10, 0, -1):
    print(n)

"""esercizio 001: calcolare x^y"""
print('\nES_001')
def potenza(x, y):
    p = 1
    for i in range(y):
        p = p * x
    print('La potenza è: ' + str(p))

x = int(input('inserisci la base: '))
y = int(input('inserisci l\'esponente: '))
potenza(x, y)
