#!/usr/bin/python3
#libs
import socket 
import os
#vars
menu = '''
1}write a file about a car licens plates
2}wirte a file about a person
3}write a file about an  ip
4}read a file (the same kind of file above) 
5}wireless attack
6}autodestruction 
7}remote injector of string
8}DDoS
9} exit
'''
passwd = "hamster"
#attacks 
def writetar():
    os.system("python3 targas.py")#ok
def writetr():
    os.system("python3 persos.py")#ok
def writeip():
    os.system("python3 ips.py")#ok
def reader():
    os.system("python3 reader.py")#ok
def wireless():
    os.system("sudo wifite")#ok
def autodist():
    os.system("gcc -o ade ade.c && chmod +x ade && ./ade")#ok
def iniezion():
    os.system("python3 DOSS.py")#ok
def ddos():
    os.system("python3 DOSmod.py")#ok
def exit():
    os.system("exit")#ok
#code
print("inserisci la password")
passphrase = input('-->')
if(passphrase==passwd):
    print(menu)
    chose = input("-->")
    if(chose=="1"):
        writetar()  
    if(chose=="2"):
        writetr()
    if(chose=="3"):
        writeip()
    if(chose=="4"):
        reader()
    if(chose=="5"):
        wireless()
    if(chose=="6"):
        autodist()
    if(chose=="7"):
        iniezion()
    if(chose=="8"):
        ddos()
    if(chose=="9"):
        exit()
else:
    print("[-]accesso negato")
