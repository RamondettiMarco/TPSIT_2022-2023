from pyfiglet import Figlet
import os
import socket, cv2, pickle,struct

os.system("clear")

pyf = Figlet(font='puffy')
#a = pyf.renderText("Video Chat App without Multi-Threading")
b = pyf.renderText("Server")

os.system("tput setaf 3")

print(b)

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)

port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen(1)
print("Listening at:",socket_address)

while True:
    client_socket,addr = server_socket.accept()
    print('Connected to:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        codifica = cv2.VideoWriter_fourcc(*'XVID')
        #imposto parametri del file video (nome del file,codifica,frame,risoluzione)
        file_video = cv2.VideoWriter("video.avi",codifica,20,(640,480))
    
    while(vid.isOpened()):
        ret,image = vid.read()
        img_serialize = pickle.dumps(image)
        message = struct.pack("Q",len(img_serialize))+img_serialize
        client_socket.sendall(message)
        if ret == True:
            # salvo frame nel file video .avi
            file_video.write(image)
            #visualizzo il frame su schermo
        cv2.imshow("WebCam",image)

        if cv2.waitKey(1) == ord('q'):
            client_socket.close()
            vid.release()
            file_video.release()
            cv2.destroyAllWindows()
            break
    
