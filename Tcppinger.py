import socket
from colored import fg
from time import sleep
from sys import exit

BANNER = f"""{fg(1)}
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""
          
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
