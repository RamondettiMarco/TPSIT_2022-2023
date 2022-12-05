#stringhe
nome = "jack"
numero = 18
nuovaStr= f"ciao {nome}, e' la lezione numero{numero}" #f = format, è il nuovo formato delle stringh che usa le {} per concatenare str
print(nuovaStr)

z = 5
ris = f"il quadrato di {z} e' {z * z}"
nuovaStr.startswith("ciao") #restituisce True o False, se inizia o no con la parola che passiamo
nuovaStr.endswith("wow") #se finise con quella parola che passiamo
nome.islower #oppure nome.isupper
#restituisce True o False, se è tutta minuscola e nel secondo se è tutta maiuscola
#metodi nome.upper() e nome.lower() per fare la str tutta maiuscola o tutta minuscola
parola = "asd"
parola.isalpha() #restituisce True o False, se è costituita solo da caratteri numerici
parola.isdecimal() #restituisce True o False, se è costituita solo da numerici
#parola.isalnum() se ci sono sia lettere che numeri, non gli altri caratteri
#parola.isspace() se c'è uno spazio
compiti = ["cane", "studio", "lavare", "spesa"]
", ".join(compiti) #crea una stringa con tutti gli elementi della lista concatenata da , e spazio
print(compiti)

daFare = "\n".join(compiti)
print(daFare)

serieNum = "1492-1984-1233331-555"
print(serieNum)
print(serieNum.split("-")) #fa la split
