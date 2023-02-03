class Packet:
    def __init__(self, comando, utente, msg):
        self.comando = comando
        self.utente = utente
        self.msg = msg
        
    def codfication(self):
        res = f"{self.comando};{self.utente};{self.msg}"
        return res.encode('utf-8')
    
    @staticmethod
    def decoding(buffer):
        str_pkt = buffer.decode('utf-8')
        campi = str_pkt.split(";")
        comando = campi[0]
        utente = campi[1]
        msg = campi[2]
        return Packet(comando, utente, msg)