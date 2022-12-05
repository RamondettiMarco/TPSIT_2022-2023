#LISTE E TUPLE

lista = [2, 5, "bacon", 3.14, "eggs"]

print(lista) #stampa tutto anche con le []

for x in lista: #ne stampa uno alla volta
    print(x)

print(lista[2]) #stampa il secondo elemento
print(lista[-1]) #stampa l'ultimo elemento
print(lista[-2]) #stampa il penultimo elemento

lista1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(lista1[3:9]) #stampa dall'elemento in posizione 3 COMPRESO all'elemento in posizione 9 NON COMPRESO

for c in range(5): #stampa i primi 5 numeri, da 0 a 4
    print(c)
    
lista3 = list(range(99,300)) #carica nella lista dal numero 99 al 299
print(lista3)

lista4 = ["a", 2, 3.14, [0, 1, 2, 3], 3.14] #una lista con una lista dentro
print(lista4)
print(lista[-2][-1]) #ultimo elemento della seconda lista, quella all'interno

lista[3] = "ciao" #posso modificare tranquillamente
del lista[3] #elimina il terzo elemento

#una tupla una volta definita non si può cancellare o modificare
tuple = (2, 4, 9, 15, 23)
print(tuple)