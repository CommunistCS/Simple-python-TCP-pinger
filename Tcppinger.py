import socket
from colored import fg
from time import sleep
from sys import exit

BANNER = f"""{fg(1)}
╔═╗┌─┐┌┬┐┌┬┐┬┌─┐
║  │ ││││││││├┤ 
╚═╝└─┘┴ ┴┴ ┴┴└─┘
          
 Made By Communist, Fuck all of u Commie Skids 


"""

def tcpping(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip,port))
        print(f"{fg(10)}Connected {fg(1)}to {fg(10)}{ip} {fg(1)}on port {fg(10)}{port}")
    except:
        print(f"{fg(1)}Connection to host lost.")

print(BANNER)
ip = input("Enter the IP to ping: ")
port = input("Enter the port to ping: ")
while True:
    try:
        tcpping(ip,int(port))
        sleep(0.7)
    except KeyboardInterrupt:
        exit(0)
