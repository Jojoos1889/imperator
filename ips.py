import os 
ip = input("ip-->")
coord = input("geographic coordinates-->")
provider = input("provider-->")
mac = input("MAC address-->")
netblock = input("netblock (192.168.1.1/x)-->")
vpn = input("vpn(True o false)-->")
tor = input("tor(True o False)-->")
print("[+]succes.")
print("[*]writing...")
file = open(ip+".txt", "w")
file.write("ip:"+ip+"\ncoordinates:"+coord+"\nprovider:"+provider+"\nmac address:"+mac+"\nnetblock:"+netblock+"\nvpn:"+vpn+"\ntor:"+tor)
