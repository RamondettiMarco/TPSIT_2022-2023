from socket import AF_INET, SOCK_DGRAM, socket

PORT = 5000
BROADCAST = "192.168.95.255"

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        msg = "hello word"
        msg = msg.encode('utf8')
        s.sendto(msg, (BROADCAST, PORT))

if __name__ == "__main__":
    chatClient()