import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
 

def portscanner():
    target = input("[*] Digite o IP para fazer o scan: ")
    port = input("[*] Digite a porta para fazer o scan: ")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"[*] Port {port} is open")
    except:
        print(f"Port {port} is closed")

portscanner()