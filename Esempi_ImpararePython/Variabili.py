x = 15 #variabile globale

def esempio():
    #se scrivo 'x' qua significa che uso una nuova variabile, sarebbe una variabile locale
    global x #non mi da errore perchè dico che uso la x variabile globale
    x += 2 #avessi messso solo questo dava errore perchè non avevo inizializzato x (variabile globale)
    return(x)

def esempio2():
    y = x #meglio non farlo, non usare la variabile globale, piuttosto passo x come parametro
    y += 2
    return(y)

def esempio3():
    s = 24
    return(s)

print(esempio())
print(esempio2())
e = esempio3() + 6
print(e)
