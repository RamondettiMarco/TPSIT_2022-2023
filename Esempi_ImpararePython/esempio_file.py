#file
import os

print(os.getcwd()) #stampa il percorso dove si sta lavorando

os.chdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python")

print(os.getcwd())

contenuto = "oggi è una bella giornata "
#lo crea in modalità scrittura "w"
file1 = open("esempio.txt", "w")
#scrivo nel file contenuto
file1.write(contenuto)

file1.close()

nuovaStr = "python è una bomba!"
#"a" = append quindi accoda, invece di riscrivere come "w"
file1 = open("esempio.txt", "a")
file1.write(nuovaStr)
file1.write("\nNuova riga")

file1.close()

varLettura = open("esempio.txt", "r").read() #legge tutto il file 
#varLettura = open("esempio.txt", "r").readlines()
#readlines() invece di read() legge riga per riga e li mette in una lista
print(varLettura)

file1.close()

