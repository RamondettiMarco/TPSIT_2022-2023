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
    
def controllo_comandi(comando, Ab):
    if comando[0].upper().startswith("W"): #avanti
        Ab.forward()
        time.sleep(int(comando[1]))        #durata del movimento
        Ab.stop()
    if comando[0].upper().startswith("D"): #destra
        Ab.right()
        time.sleep(int(comando[1]))   
        Ab.stop()
    if comando[0].upper().startswith("S"): #indietro
        Ab.backward()
        time.sleep(int(comando[1]))   
        Ab.stop()
    if comando[0].upper().startswith("A"): #sinistra
        Ab.left()
        time.sleep(int(comando[1]))   
        Ab.stop()
    if comando[0].upper().startswith("ESCI"): #fermo
        Ab.stop()

#funzione che si avvia con il comando start()
def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM) 
    s.bind(('0.0.0.0', 5000))       #bind del server tcp
    s.listen()
    Ab = AlphaBot()      #inizzializzo alphabot
    lista_comandi = []
    running = True
    
    connessione, indirizzo = s.accept()   #connessioni dei client
     
    #client = Classe_Thread(connessione, indirizzo, Ab)
    #mettere codice run
    while running:     #ciclo infinito del programma
        #print(lista_client)
        messaggio = (connessione.recv(4096)).decode("utf-8")
        durata = (connessione.recv(4096)).decode("utf-8") #ricevo il comando
        #host_collegato = (connessione.recv(4096)).decode("utf-8")

        if messaggio == 'exit':             #per chiudere il programma e scollegare i client
            running = False

            lista_client.remove()
            
        else:
            #lista_client.append(host_collegato)
            print(f"comando: {messaggio} con durata: {durata} secondi")
            comando = (messaggio, durata)
            lista_comandi.append(comando)
                    
            controllo_comandi(comando, Ab)
            
            if comando[0].upper().startswith("RIPRENDI"):
                print("Eseguo i comandi passati")
                for i in range(len(lista_comandi)-1):
                    controllo_comandi(lista_comandi[i], Ab)

    s.close()

if __name__ == "__main__":
    lista_client = []   
    main()