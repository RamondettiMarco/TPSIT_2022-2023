#1)Realizza una funzione che effettui una conversione tra date
#mantenute in tuple. La forma iniziale sarà della forma:
#(10,3,1997) per indicare la data 10/3/1997
#La forma finale dovrà essere: (decimo, Marzo,1997).
#La funzione dovrà sfruttare i dizionari.

def converti(data):
    g = dizionarioGiorno.get(data[0], 'errore')
    m = dizionarioMese.get(data[1], 'errore')
    if g == 'errore' or m == 'errore':
        dataConvertita = 'data non valida'
    else: 
        dataConvertita = (g, m, data[2])
    return dataConvertita

def traduci(chiave):
    t = dizionarioItaEng.get(chiave, 0)
    return t

dizionarioGiorno = {1: "primo", 2: "secondo", 3: "terzo", 4: "quarto", 5: "quinto", 6: "sesto", 7: "settimo", 8: "ottavo", 9: "nono",
              10: "decimo", 11: "undicesimo", 12: "dodicesimo", 13: "tredicesimo", 14: "quattordicesimo", 15: "quindicesimo",
              16: "sedicesimo", 17: "diciasettesimo", 18: "diciottesimo", 19: "diciannovesimo", 20: "ventesimo", 21: "ventunesimo",
              22: "ventiduesimo", 23: "ventitreesimo", 24: "ventiquattresimo", 25: "venticinquesimo", 26: "ventiseiesimo",
              27: "ventisettesimo", 28: "ventottesimo", 29: "ventinovesimo", 30: "trentesimo", 31: "trentunesimo"}

dizionarioMese = {1: "Gennaio", 2: "Febbraio", 3: "Marzo", 4: "Aprile", 5: "Maggio", 6: "Giugno", 7: "Luglio", 8: "Agosto",
                9: "Settembre",10: "Ottobre", 11: "Novembre", 12: "Dicembre"}

dizionarioItaEng = {"apple": "mela", "fruit": "frutta", "book": "libro", "cup": "coppa", "day": "giorno", "east": "est",
                "green": "verde","hot": "caldo", "include": "includere","lemon": "limone"}


g = int(input('inserire giorno (in numero): '))
m = int(input('inserire mese (in numero): '))
a = int(input('inserire anno (in numero): '))

#data inserita dall'utente
data = (g, m, a)
print('Data inserita: ', data)

print('Data convertita: ', converti(data))

parola = input("inserisci la parola in inglese da tradurre: ")
print("la parola tradotta è (0 se non presente): ", traduci(parola))