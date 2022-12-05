import cv2
import numpy as np
import socket

#imposto webcam che utilizzo ( '0' ==> quella interna del PC)
camera = cv2.VideoCapture(0)

#imposto codifica
codifica = cv2.VideoWriter_fourcc(*'XVID')
#imposto parametri del file video (nome del file,codifica,frame,risoluzione)
file_video = cv2.VideoWriter("video.avi",codifica,20,(640,480))

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
        #file_video = cv2.VideoWriter("video.avi",codifica,20,(640,480))

        while (camera.isOpened()):
            stato,frame = camera.read()

            if stato == True:
                # salvo frame nel file video .avi
                file_video.write(frame)
                client_socket.sendall(file_video)
                #visualizzo il frame su schermo
                cv2.imshow("WebCam",frame)

                if cv2.waitKey(1) == ord('q'):
                    #chiudo webcam, file e distruggo finestra
                    camera.release()
                    file_video.release()
                    cv2.destroyAllWindows()
                    break

