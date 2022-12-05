import csv, os
import gmaps
import gmaps.datasets
from ipywidgets.embed import embed_minimal_html
import folium
import webbrowser
import math
import pandas as pd

def create_csv_file(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Regione", "Monumento", "Coordinate", "Provincia", "Città", "Distanza", "Coordinate_Scuola")
        writer.writerow(header)
        f.close()

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()

os.chdir("C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti")
coordinateScuola = (44.37841724013469, 7.527509324729372)
listaCoordinate = [coordinateScuola]
nome = ["Itis Mario Delpozzo, Piemonte, Cuneo"]

data_file = "C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\ricerche.csv"
create_csv_file(data_file)

while(True):
    with open("./Mappa-dei-monumenti-in-Italia.csv", newline = "", encoding="ISO-8859-1") as filecsv:
        lettore = csv.reader(filecsv, delimiter = ";")
        
        counter = 0
        vetMonumeti = [""]
        numMonumento = 0
        proviMonumento = ""
        vetProvi = [""]
        counterProvi = 0
        longitudineProvi = [""]
        longitudine_FloatProvi = [0.0]
        latitudineProvi = [""]
        latitudine_FloatProvi = [0.0]
        longitudine_FloatCitta = [0.0]
        latitudine_FloatCitta = [0.0]    
        vetCitta = [""]
        vetCittaProvi = [""]
        counterCitta = 0
        reg = False
        mon = False
        provi = False
        citta = False
        asterisco = False
              
        listaRegioni = ["Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Friuli-Venezia Giulia", "Lazio", "Liguria",
                        "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "Trentino-Alto Adige",
                        "Umbria", "Valle d'Aosta", "Veneto"]
          
        while(reg == False):
            regione = input("\nInserisci la regione desiderata (* se si vogliono selezionare tutte): ")
            if(regione == "*"):
                dati = [(riga[2], riga[3], riga[8], riga[9], riga[1], riga[0]) for riga in lettore if riga[2] != "Regione" and riga[2] != "ALTRO" and riga[3] != ""]
                for monumento in dati:
                    print(f"{monumento[:2]} -- Coordinate {monumento[3]},{monumento[2]}, in Provinvia: {monumento[4]}, nella Città: {monumento[5]}")
                    longitudine = monumento[3] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    if(len(longitudine) <= 11):
                        longitudine_Float = longitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(longitudine) == 15):
                        longitudine_Float = longitudine[:-8]
                    elif(len(longitudine) == 19):
                        longitudine_Float = longitudine[:-12]
                        
                    latitudine = monumento[2]
                    if(len(latitudine) <= 11):
                        latitudine_Float = latitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(latitudine) == 15):
                        latitudine_Float = latitudine[:-8]
                    elif(len(latitudine) == 19):
                        latitudine_Float = latitudine[:-12]
                        
                    """if ((round(float(latitudine_Float), 3)/10) < 47.05 and (round(float(latitudine_Float), 3)/10) > 35.29 and (round(float(longitudine_Float), 3)/10) < 18.31 and (round(float(longitudine_Float), 3)/10) > 6.37):
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                        listaCoordinate.append(coordinate)
                        
                    else:
                        coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                        listaCoordinate.append(coordinate)"""
                        
                    if((round(float(longitudine_Float), 3)) > 6.37 and (round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) < 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3))]
                    elif((round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) < 47.05): 
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3))]
                    elif((round(float(longitudine_Float), 3)) > 6.37 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3)/10)]
                    elif((round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                    elif((round(float(longitudine_Float), 3)) < (round(float(latitudine_Float), 3))):
                        coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                    
                    listaCoordinate.append(coordinate)   
                        
                    mymap = folium.Map(location = coordinateScuola, zoom_start = 8)
                    nome.append(f"{monumento[:2]}, {monumento[4].capitalize()}, {monumento[5].capitalize()}")
                    
                    for i in range (len(listaCoordinate)):
                        folium.Marker(listaCoordinate[i], popup = nome[i]).add_to(mymap)
                    mymap.save('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\export.html')       
                    
                    distanza = math.dist(coordinateScuola, coordinate)*100
                    #print(f"La distanza tra il monumento e la scuola, in liena d'aria, è: {distanza} Km.\n")
                    
                    data = (regione, monumento[:2], coordinate, monumento[4].capitalize(), monumento[5].capitalize(), distanza, coordinateScuola)
                    add_csv_data(data_file, data)
                    
                    asterisco = True
                    mon = True
                    reg = True
            else:
                for numRegioni in range(19):
                    if(regione.upper() == listaRegioni[numRegioni].upper() or regione == "*"):
                        reg = True
            
            print("\nIl nome inserito per la regione non è valido")
                    
        dati = [(riga[2], riga[3], riga[8], riga[9], riga[1], riga[0]) for riga in lettore if riga[2] == regione.capitalize() and riga[3] != ""]
        for monumento in dati:
            print(f"{monumento[:2]} -- Coordinate {monumento[3]},{monumento[2]}") #:2 nella prima quadra vuol dire che prende i primi due(0 e 1)
            
            vetMonumeti.append("")
            vetProvi.append("")
            longitudineProvi.append("")
            longitudine_FloatProvi.append(0.0)
            latitudineProvi.append("")
            latitudine_FloatProvi.append(0.0)
            vetCitta.append("")
            vetCittaProvi.append("")   
            latitudine_FloatCitta.append(0.0)
            longitudine_FloatCitta.append(0.0)          
                    
            
        while(mon == False):
            luogo = input("\nInserire il monumento da voler visitare (* se si vogliono selezionare tutti): ")
            for monumento in dati:
                if(luogo == "*"):
                    print(f"{monumento[:2]} -- Coordinate {monumento[3]},{monumento[2]}, in Provinvia: {monumento[4]}, nella Città: {monumento[5]}")
                    
                    longitudine = monumento[3] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    if(len(longitudine) <= 11):
                        longitudine_Float = longitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(longitudine) == 15):
                        longitudine_Float = longitudine[:-8]
                    elif(len(longitudine) == 19):
                        longitudine_Float = longitudine[:-12]
                        
                    latitudine = monumento[2]
                    if(len(latitudine) <= 11):
                        latitudine_Float = latitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(latitudine) == 15):
                        latitudine_Float = latitudine[:-8]
                    elif(len(latitudine) == 19):
                        latitudine_Float = latitudine[:-12]
                        
                    """if ((round(float(latitudine_Float), 3)/10) < 47.05 and (round(float(latitudine_Float), 3)/10) > 35.29 and (round(float(longitudine_Float), 3)/10) < 18.31 and (round(float(longitudine_Float), 3)/10) > 6.37):
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                        listaCoordinate.append(coordinate)
                        
                    else:
                        coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                        listaCoordinate.append(coordinate)"""
                    
                    if((round(float(longitudine_Float), 3)) > 6.37 and (round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) < 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3))]
                    elif((round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) < 47.05): 
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3))]
                    elif((round(float(longitudine_Float), 3)) > 6.37 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3)/10)]
                    elif((round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                        coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                    elif((round(float(longitudine_Float), 3)) < (round(float(latitudine_Float), 3))):
                        coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                    
                    listaCoordinate.append(coordinate)
                    
                    mymap = folium.Map(location = coordinateScuola, zoom_start = 8)
                    nome.append(f"{monumento[:2]}, {monumento[4].capitalize()}, {monumento[5].capitalize()}")
                    
                    for i in range (len(listaCoordinate)):
                        folium.Marker(listaCoordinate[i], popup = nome[i]).add_to(mymap)
                    mymap.save('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\export.html')       
                    
                    distanza = math.dist(coordinateScuola, coordinate)*100
                    print(f"La distanza tra il monumento e la scuola, in liena d'aria, è: {distanza} Km.\n")
                    
                    data = (regione,  monumento[:2], coordinate, monumento[4].capitalize(), monumento[5].capitalize(), distanza, coordinateScuola)
                    add_csv_data(data_file, data)
                    
                    asterisco = True
                    mon = True 
                        
                elif(monumento[1].upper() == luogo.upper()):
                    if(counter <= 1):
                        print(f"\nIl monumento scelto è:  {monumento[1]}, in Provinvia: {monumento[4]}, nella Città: {monumento[5]} -- con Coordinate: {monumento[3]},{monumento[2]}")
                        longitudine = monumento[3] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                        latitudine = monumento[2]
                        
                    else:
                        print(f"Il monumento scelto è:  {monumento[1]}, in Provinvia: {monumento[4]} -- con Coordinate: {monumento[3]},{monumento[2]}")
                    
                    vetMonumeti[counter] = monumento[1]
                    vetProvi[counter] = monumento[4]
                    vetCitta[counter] = monumento[5]
                    
                    longitudine = monumento[3] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    if(len(longitudine) <= 11):
                        longitudine_Float = longitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(longitudine) == 15):
                        longitudine_Float = longitudine[:-8]
                    elif(len(longitudine) == 19):
                        longitudine_Float = longitudine[:-12]
                        
                    latitudine = monumento[2]
                    if(len(latitudine) <= 11):
                        latitudine_Float = latitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(latitudine) == 15):
                        latitudine_Float = latitudine[:-8]
                    elif(len(latitudine) == 19):
                        latitudine_Float = latitudine[:-12]
                    
                    longitudineProvi[counter] = monumento[3] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    if(len(longitudineProvi[counter]) <= 11):
                        longitudine_FloatProvi[counter] = longitudineProvi[counter][:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(longitudineProvi[counter]) == 15):
                        longitudine_FloatProvi[counter] = longitudineProvi[counter][:-8]
                    elif(len(longitudineProvi[counter]) == 19):
                        longitudine_FloatProvi[counter] = longitudineProvi[counter][:-12]
                        
                    latitudineProvi[counter] = monumento[2]
                    if(len(latitudineProvi[counter]) <= 11):
                        latitudine_FloatProvi[counter] = latitudineProvi[counter][:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                    elif(len(latitudineProvi[counter]) == 15):
                        latitudine_FloatProvi[counter] = latitudineProvi[counter][:-8]
                    elif(len(latitudineProvi[counter]) == 19):
                        latitudine_FloatProvi[counter] = latitudineProvi[counter][:-12]
                        
                    counter += 1
                    mon = True
                  
            if(counter > 1):
                while(provi == False):
                    proviMonumento = input(f"\nIl monumento scelto:  {monumento[1]} ha avuto più risultati, scegliere la provincia desiderata: ")
                    for i in range(counter):
                        if(proviMonumento.upper() == vetProvi[i]):
                            longitudine_FloatCitta[counterProvi] = longitudine_FloatProvi[i]   
                            latitudine_FloatCitta[counterProvi] = latitudine_FloatProvi[i]
        
                            print(f"Il monumento selezionato è:  {vetMonumeti[int(numMonumento)]}, in Provinvia: {vetProvi[i]}, nella Città: {vetCitta[i]} -- Coordinate {longitudine_FloatProvi[i]} , {latitudine_FloatProvi[i]}")
                            provi = True
                            vetCittaProvi[counterProvi] = vetCitta[i]
                            counterProvi += 1                    
                            
                    if(counterProvi == 0):
                        print(f"\nLa provincia inserita: --{proviMonumento}-- non è presente in {regione.capitalize()}")    
                    elif(counterProvi == 1):
                        """if ((round(float(latitudine_FloatProvi[i]), 3)/10) < 47.05 and (round(float(latitudine_FloatProvi[i]), 3)/10) > 35.29 and (round(float(longitudine_FloatProvi[i]), 3)/10) < 18.31 and (round(float(longitudine_FloatProvi[i]), 3)/10) > 6.37):
                            coordinate = [(round(float(longitudine_FloatProvi[i]), 3)/10), (round(float(latitudine_FloatProvi[i]), 3)/10)]
                            listaCoordinate.append(coordinate)
                        else:
                            coordinate = [(round(float(latitudine_FloatProvi[i]), 3)/10), (round(float(longitudine_FloatProvi[i]), 3)/10)]
                            listaCoordinate.append(coordinate)"""
                        
                        if((round(float(longitudine_Float), 3)) > 6.37 and (round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) < 47.05):
                            coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3))]
                        elif((round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) < 47.05): 
                            coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3))]
                        elif((round(float(longitudine_Float), 3)) > 6.37 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                            coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3)/10)]
                        elif((round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                            coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                        elif((round(float(longitudine_Float), 3)) < (round(float(latitudine_Float), 3))):
                            coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                            
                        listaCoordinate.append(coordinate)
                            
                        mymap = folium.Map(location = coordinateScuola, zoom_start = 8)
                        nome.append(f"{luogo.capitalize()}, {proviMonumento.capitalize()}, {vetCitta[i].capitalize()}")    
                        cittaMonumento = vetCitta[i]
                                                            
                        for i in range (len(listaCoordinate)):
                            folium.Marker(listaCoordinate[i], popup = nome[i]).add_to(mymap)
                        
                        for i in range (len(listaCoordinate)):
                            folium.PolyLine(locations = [listaCoordinate[i], listaCoordinate[0]], lone_opacity = 0.5).add_to(mymap)
                        mymap.save('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\export.html')
                        
                    elif(counterProvi > 1):
                        while(citta == False):
                            cittaMonumento = input(f"\nLa provincia scelta: {proviMonumento}, per il monumento scelto: {monumento[1]}, ha avuto più risultati, scegliere la citta: ")
                            for c in range(counterProvi):
                                if(cittaMonumento.upper() == vetCittaProvi[c]):
                                    counterCitta += 1
                                    print(f"Il monumento selezionato è:  {vetMonumeti[int(numMonumento)]}, in Provinvia: {proviMonumento.upper()}, nella Città: {vetCittaProvi[c]} -- Coordinate {longitudine_FloatCitta[c]} , {latitudine_FloatCitta[c]}")
                                    citta = True
                                    
                            if(counterCitta == 0):
                                print(f"\nLa citta inserita: --{cittaMonumento}-- non è presente in {proviMonumento.upper()}")
                            else:
                                """if ((round(float(latitudine_FloatCitta[c]), 3)/10) < 47.05 and (round(float(latitudine_FloatCitta[c]), 3)/10) > 35.29 and (round(float(longitudine_FloatCitta[c]), 3)/10) < 18.31 and (round(float(longitudine_FloatCitta[c]), 3)/10) > 6.37):
                                    coordinate = [(round(float(longitudine_FloatCitta[c]), 3)/10), (round(float(latitudine_FloatCitta[c]), 3)/10)]
                                    listaCoordinate.append(coordinate)
                                else:
                                    coordinate = [(round(float(latitudine_FloatCitta[c]), 3)/10), (round(float(longitudine_FloatCitta[c]), 3)/10)]
                                    listaCoordinate.append(coordinate)"""
                                    
                                if((round(float(longitudine_Float), 3)) > 6.37 and (round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) < 47.05):
                                    coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3))]
                                elif((round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) < 47.05): 
                                    coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3))]
                                elif((round(float(longitudine_Float), 3)) > 6.37 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                                    coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3)/10)]
                                elif((round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                                    coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                                elif((round(float(longitudine_Float), 3)) < (round(float(latitudine_Float), 3))):
                                    coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                                
                                listaCoordinate.append(coordinate)
                                    
                                mymap = folium.Map(location = coordinateScuola, zoom_start = 8)
                                nome.append(f"{luogo.capitalize()}, {proviMonumento.capitalize()}, {cittaMonumento.capitalize()}")
                        
                                for i in range (len(listaCoordinate)):
                                    folium.Marker(listaCoordinate[i], popup = nome[i]).add_to(mymap)
                                
                                for i in range (len(listaCoordinate)):
                                    folium.PolyLine(locations = [listaCoordinate[i], listaCoordinate[0]], lone_opacity = 0.5).add_to(mymap)
                                mymap.save('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\export.html')

                    elif(counterProvi == 0):
                            print(f"\nLa provincia inserita: --{proviMonumento.upper()}-- non ha un {luogo.upper()}")
                        
            elif(counter == 0 and asterisco == False):
                        print(f"\nIl monumento inserito: --{luogo.upper()}-- non è presente in {regione.capitalize()}")
                    
            elif(counter == 1):
                if(len(longitudine) <= 11):
                    longitudine_Float = longitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                elif(len(longitudine) == 15):
                    longitudine_Float = longitudine[:-8]
                elif(len(longitudine) == 19):
                    longitudine_Float = longitudine[:-12]
                    
                if(len(latitudine) <= 11):
                    latitudine_Float = latitudine[:-4] #tolgo le ultime 3 cire e l'ultimo punto per poi riuscire ad avere un float
                elif(len(latitudine) == 15):
                    latitudine_Float = latitudine[:-8]
                elif(len(latitudine) == 19):
                    latitudine_Float = latitudine[:-12]
                 
                cittaMonumento = monumento[5]
                proviMonumento = monumento[4]
                
                """if ((round(float(latitudine_Float), 3)/10) < 47.05 and (round(float(latitudine_Float), 3)/10) > 35.29 and (round(float(longitudine_Float), 3)/10) < 18.31 and (round(float(longitudine_Float), 3)/10) > 6.37):
                    coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                    listaCoordinate.append(coordinate)
                else:
                    coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                    listaCoordinate.append(coordinate)"""
                
                if((round(float(longitudine_Float), 3)) > 6.37 and (round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) < 47.05):
                    coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3))]
                elif((round(float(latitudine_Float), 3)) > 35.29 and (round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) < 47.05): 
                    coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3))]
                elif((round(float(longitudine_Float), 3)) > 6.37 and (round(float(longitudine_Float), 3)) < 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                    coordinate = [(round(float(longitudine_Float), 3)), (round(float(latitudine_Float), 3)/10)]
                elif((round(float(longitudine_Float), 3)) > 18.31 and (round(float(latitudine_Float), 3)) > 47.05):
                    coordinate = [(round(float(longitudine_Float), 3)/10), (round(float(latitudine_Float), 3)/10)]
                elif((round(float(longitudine_Float), 3)) < (round(float(latitudine_Float), 3))):
                    coordinate = [(round(float(latitudine_Float), 3)/10), (round(float(longitudine_Float), 3)/10)]
                
                listaCoordinate.append(coordinate)
                    
                mymap = folium.Map(location = coordinateScuola, zoom_start = 8)
                nome.append(f"{luogo.capitalize()}, {monumento[4].capitalize()}, {monumento[5].capitalize()}")
                    
                for i in range (len(listaCoordinate)):
                    folium.Marker(listaCoordinate[i], popup = nome[i]).add_to(mymap)
                
                for i in range (len(listaCoordinate)):
                    folium.PolyLine(locations = [listaCoordinate[i], listaCoordinate[0]], lone_opacity = 0.5).add_to(mymap)
                mymap.save('C:\\Users\\utente\\Desktop\\ITIS\\TPSIT\\Python\\Esercizio_Monumenti\\export.html')

        if(asterisco == False):
            distanza = math.dist(coordinateScuola, coordinate)*100
            print(f"La distanza tra il monumento e la scuola, in liena d'aria, è: {distanza} Km.\n")
            data = (regione.capitalize(), luogo.capitalize(), coordinate, proviMonumento.capitalize(), cittaMonumento.capitalize(), distanza, coordinateScuola)
        
        fine = input('\nTERMINARE IL PROGRAMMA? (s/n)')
        if(fine.upper() == 'S'):
            if input('\nVisualizzare le ricerche effettuate? (s/n)').upper() == 'S':
                print('ricerche effettuate: ', listaCoordinate)
            
            add_csv_data(data_file, data)    
            print('\n--PROGRAMMA TERMINATO--')
            print("--DATI SALVATI SU: ricerche.csv")
            
            webbrowser.open_new_tab("export.html")
            
            break
        
        elif(fine.upper() == 'N'):
            print('\n----------------------------------------------------------------')
            print("NUOVO INSERIMENTO: ")  
          
    filecsv.close()