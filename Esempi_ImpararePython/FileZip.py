import os, zipfile

archivio =  zipfile.ZipFile("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\archivioEs.zip", "w") # w sovrascrive

os.chdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python")

archivio.write("esempio.txt", compress_type = zipfile.ZIP_DEFLATED)
archivio.close()

archivio =  zipfile.ZipFile("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\archivioEs.zip", "a") #a aggiunge
archivio.write("esempio2.txt", compress_type = zipfile.ZIP_DEFLATED)
archivio.write("esempio3.txt", compress_type = zipfile.ZIP_DEFLATED)
archivio.close()

archivio =  zipfile.ZipFile("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\archivioEs.zip") #senza a e w legge
archivio.extractall("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\cartella_estrazione") #estrae tutto
#archivio.extract("esempio.txt", "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\cartella_estrazione") # ne estrae solo uno, quello che passp

text_info = archivio.getinfo("esempio.txt")
print(text_info.file_size)

print(text_info.compress_size)

archivio.close()
