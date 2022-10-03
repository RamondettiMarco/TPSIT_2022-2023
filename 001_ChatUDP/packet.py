# | 1byte (lunghezza_username) | username | 2byte (lunghezza_msg) | msg

class Packet:
    def __init__(self, username, msg):
        #validazione
        self.username = username
        self.msg = msg
    
    def to_bytes(self):
        buffer = b'' #tipo bytes
         
        username_bytes = self.username.encode('utf-8')
        buffer = len(username_bytes).to_bytes(1, 'big')
        buffer = buffer + username_bytes
        
        msg_bytes = self.msg.encode('utf-8')
        buffer = buffer + len(msg_bytes).to_bytes(2, 'big')
        buffer = buffer + msg_bytes
        
        return buffer
    
    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1:username_size+1].decode('utf-8')
        
        msg_size = int.from_bytes(buffer[username_size+1:username_size+3], 'big')
        msg = buffer[username_size+3:username_size+3+msg_size].decode('utf-8')
        
        return Packet(username, msg)

def run_tests(): #test unitari
    pkt0 = Packet("usr", "msg")
    pkt1 = Packet.from_bytes(pkt0.to_bytes())
    assert(pkt0.msg == pkt1.msg)    #ad assert devo passare qualcosa di vero se no da errore
    assert(pkt0.username == pkt1.username)
    
if __name__ == '__main__':
    run_tests()