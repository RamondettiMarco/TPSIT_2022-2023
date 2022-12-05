import time

class AlphaBot(object):  #classe dell'Alfabot
    
    def __init__(self):
        print("Inizializzazione AlphaBot")

    def backward(self):  #avanti a velocità 60
        print("Va indietro")


        
    def stop(self):     #fermare i motori
        print("Fermo")

    def forward(self):   #indietro velocità 60
        print("Va avanti")
        
        

    def left(self):     #girare a sinistra velocità settata in precedenza
        print("Gira a sinistra")
    
    
    def right(self):    #destra con la velocità settata in precedenza
        print("Gira a destra")
        
    def set_pwm_a(self, value):
        print("Setta pwm_a")

    def set_pwm_b(self, value):
        print("Setta pwm_b") 
        
    def set_motor(self, left, right):
        print("Setta i motori")