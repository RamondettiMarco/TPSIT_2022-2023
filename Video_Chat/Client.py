from pyfiglet import Figlet
import socket,cv2, pickle,struct
import os

os.system("clear")

pyf = Figlet(font='puffy')
a = pyf.renderText("Video Chat App without Multi-Threading")
b = pyf.renderText("Client")

os.system("tput setaf 3")

print(b)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.56.1' 
port = 9999
client_socket.connect((host_ip,port)) 
data = b""
metadata_size = struct.calcsize("Q")

while True:
    print(len(data))
    print(metadata_size)
    while len(data) < metadata_size:
        packet = client_socket.recv(4*1024) 
        """if not packet: 
            break
        data += packet
        print(data.decode())
        packed_msg_size = data[:metadata_size]
        data = data[metadata_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data  = data[msg_size:]"""
        frame = pickle.loads(packet)
        cv2.imshow("Receiving Video ",frame)
        
    key = cv2.waitKey(10) 
    if key  == 13:
        break
client_socket.close()