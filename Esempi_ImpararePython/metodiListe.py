#metodi liste
inventario = ["torcia", "spada", "pane", "arco"]
inventario.append("frecce") #append aggiunge un elemento nella lista
print(inventario)

def riempiInventario():
    inventario = []
    while True:
        oggetto = input("cosa vuoi aggiungere all'inventario ('terminato' se vuoi finire)?")
        if(oggetto == "terminato"):
            break
        else:
            inventario.append(oggetto)
    print("gli oggetti dell'inventario sono: ", inventario)

#riempiInventario()

inventario.remove("arco") #rimuove arco
print(inventario)

alfabeto = ["a", "c", "b", "h", "e", "f", "g", "d"]
alfabeto.sort() #mette in ordine, funziona anche con lista numerica
print(alfabeto)

alfabeto.sort(reverse=True) #mette in ordine contrario de
print(alfabeto)

print(alfabeto.index("a")) #dice in che posizione si trova l'elemento che passo

alfabeto.insert(2, "ciao") #inserisco un elemento nella posizione che voglio
print(alfabeto)
