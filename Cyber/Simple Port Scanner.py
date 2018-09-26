import socket
def scanner(host,port):
    try:
        s.connect((host,port))
        return True
    except:
        return False
s = socket.socket()
host = input("Enter IP address or website: ")
hostIP = socket.gethostbyname(host)
for port in range(1,3390):
    if scanner(hostIP,port):
        print("\033[32m[+] \033[30mPort {} is Open.".format(port))
    else:
        print("\033[31m[-] \033[30mPort {} is Closed.".format(port))
        continue
