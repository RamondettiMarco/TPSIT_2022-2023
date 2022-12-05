#file
import shutil
import os

shutil.copy("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\esempio.txt", "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT") #copia e stampa dove lo ha spostato

shutil.move("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\esempio.txt", "C:\\Users\\utente\\Desktop") #lo sposta

os.unlink("C:\\Users\\utente\\Desktop\\esempio.txt") #unlink potentissimo, elimina permanentemente
#os.rename("C:\\Users\\utente\\Desktop\\esempio.txt", "C:\\Users\\utente\\Desktop\\esempioModificato.txt") #rinomina