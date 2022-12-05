import csv
from numbers import Integral
from operator import le
import os
import matplotlib.pyplot as plt
import numpy as np

def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Paese", "Media Consumo CO2")
        writer.writerow(header)
        f.close()

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)
        f.close()

os.chdir('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_CO2')
print('INIZIO PROGRAMMA - CAMBIAMENTO CLIMATICO')

data_file = "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_CO2\\salvataggio.csv"
create_csv_file(data_file)

listaPaesi = []

nomeStati = []

with open('./owid-co2-data.csv', newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv, delimiter = ",")
    header = next(lettore)
    #print(header)
    
    dati = [(riga[1], riga[2], riga[3], riga[4]) for riga in lettore if riga[1] != "" and riga[2] != "" and riga[3] != "" and riga[4] != ""]

    for paese in dati:
        if not paese[0] in nomeStati:
            nomeStati.append(paese[0])
        
    for i in range(len(nomeStati)):
        listaPaesi.append([])
        for paese in dati:
            if paese[0] == nomeStati[i]:
                listaPaesi[i].append(paese)

    co2Totale = []
    media = 0
    pointp = []
    anno = []

    for i in range (len(listaPaesi)):
        c = 0
        pointp = []
        anno = []
        for k in range (len(listaPaesi[i])):
            #print(listaPaesi[i][k][0] + ',' + listaPaesi[i][k][2])
            numero = listaPaesi[i][k][3]
            media = media + float(numero)
            c += 1
            pointp.append(float(numero))
            anno.append(float(listaPaesi[i][k][1]))
        media = media / c
        co2Totale.append(float(media))
        print(listaPaesi[i][k][0] + ',' + str(media))

        data = (listaPaesi[i][k][0], media)

        add_csv_data(data_file, data)    
    
    
    #print(co2Totale)
    """point = np.array(co2Totale)
    plt.plot(point)
    n, bins, patches=plt.hist(nomeStati, bins = len(nomeStati), density = True)
    plt.xlabel("Paese")
    plt.ylabel("CO2")
    plt.title("Diagramma consumo")
    plt.xticks(rotation=90)
    plt.show()"""
    paese = False

    while(paese == False):
        p = input("\nInserisci il paese ricercato (* se li vuoi vedere insieme): ")
        if(p == '*'):
            point = np.array(co2Totale)
            plt.plot(point)
            #n, bins, patches=plt.hist([x for x in nomeStati], bins = len(nomeStati), density = True)
            plt.xlabel("Paese")
            plt.ylabel("CO2")
            plt.title("Diagramma consumo")
            plt.xticks(rotation = 90)
            ax = plt.subplot()
            ax.bar(nomeStati, co2Totale)
            plt.savefig("Completo.png")
            plt.show()
            paese = True

        for i in range(len(listaPaesi)):
            if(p.capitalize() == nomeStati[i]):
                plt.clf()
                plt.xlabel(p.capitalize())
                plt.ylabel("CO2")
                plt.title("Diagramma consumo " + p.capitalize())
                plt.plot(anno, pointp)
                plt.savefig(f"{p.capitalize()}.png")
                plt.show()
                paese = True
        
    print('\n--PROGRAMMA TERMINATO--')
    print("--DATI SALVATI SU: salvataggio.csv")
    
filecsv.close()


