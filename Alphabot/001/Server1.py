#!/usr/bin/python
# _*_ coding: utf-8 -*-
#server tpc

import socket as sck
import threading as thr
import time
from Alphabot1 import AlphaBot
import RPi.GPIO as GPIO
#import sqlite3 #libreria data base

TEMPO_PER_CURVARE_DI_90_GRADI = 0.5

#classe thread
#funzione che si avvia alla creazione della classe
def __init__(self, connessione, indirizzo ,alphabot):
    thr.Thread.__init__(self)   #costruttore super (java)
    self.connessione = connessione
    self.indirizzo=indirizzo
    self.alphabot=alphabot          #per usare la classe del robot all'interno del thread
    self.running = True

#funzione che si avvia con il comando start()
def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM) 
    s.bind(('0.0.0.0', 5000))       #bind del server tcp
    s.listen()
    Ab = AlphaBot()      #inizzializzo alphabot

    running = True
    
    connessione, indirizzo = s.accept()   #connessioni dei client
     
    #client = Classe_Thread(connessione, indirizzo, Ab)
    #mettere codice run
    while running:     #ciclo infinito del programma
        
        messaggio = (connessione.recv(4096)).decode("utf-8")
        durata = (connessione.recv(4096)).decode("utf-8") #ricevo il comando

        if messaggio == 'exit':             #per chiudere il programma e scollegare i client
            running = False

            lista_client.remove()
            
        else:
            print(f"comando: {messaggio} con durata: {durata} secondi")
                    
            if messaggio.upper().startswith("W"): #avanti
                Ab.forward()
                time.sleep(int(durata))        #durata del movimento
                Ab.stop()
            if messaggio.upper().startswith("D"): #destra
                Ab.right()
                time.sleep(int(durata))   
                Ab.stop()
            if messaggio.upper().startswith("S"): #indietro
                Ab.backward()
                time.sleep(int(durata))   
                Ab.stop()
            if messaggio.upper().startswith("A"): #sinistra
                Ab.left()
                time.sleep(int(durata))   
                Ab.stop()
            if messaggio.upper().startswith("ESCI"): #fermo
                Ab.stop()

    s.close()

if __name__ == "__main__":
    lista_client = []   
    main()