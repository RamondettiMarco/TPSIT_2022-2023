import os

os.chdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python") #ci spostiamo in <percorso>
print(os.listdir())

for cartella, sottocartella, files in os.walk(os.getcwd()):
    print(f"ci troviamo nella cartella: {cartella}")
    print(f"le sottocartelle sono {sottocartella}")
    #print(f"i files sono {files} \n")
    for file in files:
        if file.endswith(".py"):
            print("file python: {file}")
    print()