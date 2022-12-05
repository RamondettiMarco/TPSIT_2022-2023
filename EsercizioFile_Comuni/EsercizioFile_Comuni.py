file = open("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\EsercizioFile_Comuni\\regpie-Limiti_amm_pop_9908-all.csv", "r").readlines()

c = 1 #perchè l'intestazione è esclusa
for x in file:
    #print(x)
    c += 1
print(c)