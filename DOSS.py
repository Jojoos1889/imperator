import socket
w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d= input("string to inject-->")
db = bytes(d,"utf-8")
ip = "209.124.145.124"
port = 502
w.connect((ip, port))
print("[+]sended")
w.send(db)
