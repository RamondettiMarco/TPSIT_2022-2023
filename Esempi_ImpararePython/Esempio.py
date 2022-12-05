from ssl import _create_default_https_context


lista = [5, 6, 7, 8, 9, 10, 11]
for x in lista: #FOR
    print(x) #stampa tutti gli elementi in colonna
    
print("lunghezza: ", len(lista))
#print(len(lista))

s = 'Ciao di dove sei?' #singoli o doppi apici è uguale
print(s) #stampo la stringa
print(s[3]) #solo il terzo carattere
print(s[9:11]) #dal carattere 9 al carattere 11
print(6 in lista) #controllo se l'elemento 6 esiste nella lista, stampa un booleano

#comando "type(x)" ci dice quale sia il tipo della veriabile x

cit = "ciao mi chiao \"Ramo\"" #per usare le vitgolette nelle frasi
print(cit)

eta = input("inserisci età: ") #per chiedere input da tastiera

print("età: " + str(eta)) #str converte un intero in una stringa, serve per concatenare
esempio = '27'
print(esempio * 3)
print(int(esempio) * 3) #"int" converte stringa in int

patente = False
if(int(eta) >= 18 and patente == True): #IDENTAZIONE e ":"
    print("sei magiorenne, puoi noleggiare una macchina")
elif(int(eta) >= 18 and patente == False): #elif = else if
    print("sei maggiorenne, ma non puoi noleggiare una macchina")
else: 
    print("sei minorenne")
    
contatore = 0
while(contatore <= 10): #WHILE
    print(contatore)
    contatore += 1 #è uguale a contatore++ ma su python si scrive contatore += 1
    #contatore = contatore + 1 -> stessa cosa che sopra
 
i = 0   
while(True): #ciclo infinito, loop di controllo, per bloccarlo CTRL+C
    #print("ciclo infinito")
    i += 1
    if(i > 10):
        print("sto uscendo dal loop!")
        break

cnt = 0
while(cnt < 10):
    cnt += 1
    if(cnt == 3):
        print("valore saltato")
        continue
    print(cnt)
    