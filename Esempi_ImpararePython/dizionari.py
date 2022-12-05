#dizionari
#ad ogni valore è associata una chiave, una specie di indice
dizionario = {"chiave1": "valore1", "eta": 17, 3.14: "pi_greco", "primi": [1, 2, 3, 5, 7]}

print(dizionario["chiave1"]) #stampo il valore associato alla chiave
print(dizionario[3.14])

dizionario["chiave2"] = "valore2" #aggiungo un valore ad una nuova chiave
dizionario["eta"] = 99 #modifico il valore corrispondente alla chiave eta

print(dizionario)

#i dizionari sono elenchi di valori non ordinative
#2 dizionari sono uguali se hanno gli stessi valori con le stesse chiavi, indipendentemente dall'ordine

print("primi" in dizionario) #per vedere se c'è questa chiave
print("zen" in dizionario)

del dizionario["chiave1"] #elimina la chiave e quello a cui è associata

itaEng = {"ciao": "hello", "gatto": "cat", "uova": "eggs", "arancia": "orange", "arrivederci": "goodby"}
print(itaEng.keys()) #stampa tutte le chiavi el dizionario
print(itaEng.values()) #stampa tutti i valori ch sono associati a delle parole chiave
print(itaEng.items()) #stampa tutte le chiav e le parole associate

paroleEng = list(itaEng.values()) #metto i valori in una lista
print("parole inglesi: ", paroleEng) 

for chiave in itaEng.keys(): #stampa tutte le chiavi, una per volta
    print(chiave)
    
#se uso una chiave che non esiste da un errore: KeyError
if "birra" in itaEng.keys():
    print(itaEng["birra"])
else:
    print("chiave non trovata")
    
print(itaEng.get("birra", "chiave non trovata mi spiace")) #fa esattamente la stessa cosa del if precedente grazie al get
print(itaEng.get("ciao", "chiave non trovata mi spiace"))

itaEng.setdefault("birra", "beer") #aggiunge al dizionario
print(itaEng)
