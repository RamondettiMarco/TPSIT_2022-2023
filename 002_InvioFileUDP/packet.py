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
        status = self.status.to_bytes(1, 'big')
        size = len(self.data)
        size = size.to_bytes(2, 'big')
        
        return status + size +self.data
    
    @staticmethod
    def from_bytes(buffer):
        status = int.from_bytes(buffer[:1], 'big')
        msg_size = int.from_bytes(buffer[1:3], 'big')
        data = buffer[3:3+msg_size]
        
        return Packet(status, data)

def run_tests(): #test unitari
    pkt0 = Packet("usr", "msg")
    pkt1 = Packet.from_bytes(pkt0.to_bytes())
    assert(pkt0.msg == pkt1.msg)    #ad assert devo passare qualcosa di vero se no da errore
    assert(pkt0.username == pkt1.username)
    
if __name__ == '__main__':
    run_tests()