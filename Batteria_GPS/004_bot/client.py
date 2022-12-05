from base64 import encode
from encodings import utf_8
from http.client import SWITCHING_PROTOCOLS
from msilib.schema import RemoveIniFile
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from plyer import battery
from threading import Thread
import csv
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
"""ip = input('Inserisci l\'indirizzo IP del server: ')
port = input('Inserisci la porta: ')"""
ip = "192.168.1.12"
port = 888

#s.bind((ip, port))

#BATTERIA
batteria = []

class ReceiveThread(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        print('init')
    
    def run(self):
        i = 0
        while True:
            print('Server listening...')
            data, addr = s.recvfrom(4096)
            print('client'+data.decode('utf-8'))
            stringa = str(data.decode('utf-8'))
            lista = stringa.split(',')
            print(lista[0])
            messaggio = lista[0]
            """data = self.socket.recvfrom(1024)
            message = data[0].decode()
            ip_address = data[1][0]
            port_boh = int(data[1][1])"""
            if messaggio == 'batteria':     #
                print('dentro')
                batteria.clear()
                batteria.append(lista[1])
                batteria.append(lista[2])

            if messaggio == 'exit':
                print('Connessione chiusa.')        #!CHIUDO LA CONNESSIONE TRA CLIENT E SERVER
                break

        self.socket.close()


class MainWindow(BoxLayout):
    Builder.load_file("interfaccia_client.kv")
    
    inCarica = ObjectProperty(None)
    percentualeBatteria = ObjectProperty(None)

    def send(self, istruzione):
        #istruzione = "batteria"
        ip = '127.0.0.1'
        port = 888
        #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(istruzione.encode('utf-8'), (ip, port))
        """self.inCarica.text = str(battery.status['isCharging'])
        self.percentualeBatteria.text = str(battery.status['percentage']) + "%"
        """
        ReceiveThread(s).start()

    def batteria(self):
        self.inCarica.text = batteria[0]
        self.percentualeBatteria.text = batteria[1]
        

class Client(MDApp):
    def build(self):
        self.title = 'CLIENT'
        return MainWindow()     


Client().run()