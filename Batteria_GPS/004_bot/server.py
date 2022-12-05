#socket UDP
from audioop import cross
import socket
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from plyer import battery

def clear_create_file():
    #svuoto il file csv
    with open('dati.csv', 'w') as filecsv:
        writer = csv.writer(filecsv)
        writer.writerow(["IP", "PORTA", "MESSAGGIO"])
        filecsv.close()

def to_file(ip, port, message):
    with open('dati.csv', 'a') as filecsv:
        writer = csv.writer(filecsv)
        dati = (ip, port, message)
        writer.writerow(dati)   
        filecsv.close()

clear_create_file()



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
"""ip = input('Inserisci l\'indirizzo IP del server: ')
port = input('Inserisci la porta: ')"""
ip = "127.0.0.1"    #?192.168.1.12
port = 888

s.bind((ip, port))

while True:
    print('Server listening...')
    data = s.recvfrom(4096)
    message = data[0].decode()

    ip_address = data[1][0]
    port_boh = int(data[1][1])
    
    print(data, message, ip_address, port_boh)
    print(message)

    if message == 'batteria':
        stato = str(battery.status['isCharging'])
        percentuale = str(battery.status['percentage']) + "%"
        dato = 'batteria' + ',' + stato + ',' + percentuale
        print(dato)
    
    if message == 'exit':
        dato = 'exit'
        print("Connessione chiusa.")
        break
    
    #to_file(ip_address, port_boh, message)
    print('MESSAGE ' + message)
    s.sendto(dato.encode(), (ip_address, int(port_boh)))

s.close()