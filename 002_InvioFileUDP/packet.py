# | 1byte (lunghezza_username) | username | 2byte (lunghezza_msg) | msg

class Packet:
    NEW_FILE = 0
    GO_ON = 1
    END_FILE = 2
    def __init__(self, status, data):
        #validazione
        self.status = status
        self.data = data
    
    def to_bytes(self):
        status = self.status.to_bytes(1, 'big') #se è l'ultimo pacchetto se è nuovo NEW_FILE quindi 0, ecc -> guarda attributi classe
        size = len(self.data)
        size = size.to_bytes(2, 'big') # il 2 o l'1 prima si riferiscono ai bytes che dedice 
        
        return status + size + self.data
    
    @staticmethod
    def from_bytes(buffer):
        status = int.from_bytes(buffer[:1], 'big')
        msg_size = int.from_bytes(buffer[1:3], 'big')
        data = buffer[3:3+msg_size]
        
        return Packet(status, data)