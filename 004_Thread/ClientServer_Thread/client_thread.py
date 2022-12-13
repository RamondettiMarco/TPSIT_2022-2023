import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    client.sendall("4*5".encode("utf-8"))
    response = client.recv(4096).decode("utf-8")
    print(response)

if __name__ == "__main__":
    main()