import os, shutil

print(os.getcwd()) #ci dice in che cartella siamo

print(os.listdir()) #ci dice le cartelle che ho nel percorso in cui mi trovo

os.chdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python") #ci spostiamo in <percorso>

os.makedirs("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\lezioneFile") #crea una cartella

os.rename("lezioneFile", "LezioneFile") #rinomina una cartella

print(os.listdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python")) #per vedere se ha creato la cartella

shutil.move("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\LezioneFile", "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esempi_ImpararePython") #sposta
#shutil.copytree() copia tutto anche il contenuto del
shutil.rmtree("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esempi_ImpararePython\\LezioneFile") #cancella tutto il contnuto di quello che passo


