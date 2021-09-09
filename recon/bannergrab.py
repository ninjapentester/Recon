#!/usr/bin/python3

# Basic banner grabbing script,created by Mattia Campagnano on Thu 09 Sep 2021 08:14:48 AM EDT
# The banner grabbing function is based on code taken from TJ O'Connor's Violent Python 

import sys
import socket


# banner grabbing function
              
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner

    except:
        return

# Basic script functioning. IP addresses are grabbed from an input file.



def main():
   if len(sys.argv) == 2:
      file = sys.argv[1]

   for port in range(21,26):
  
        #print(port)
    
          
        with open(file,'r') as f:

                for line in f:
                    ip=line.strip()
                    #print(ip, port)
                    banner = retBanner(ip, port)

# Grab the banner and display it along with IP address and port   

                    print(ip,port)
                    print(banner)
              
                    
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             
                socket.setdefaulttimeout(5)
                result = s.connect_ex((ip,port))

                if result==0:
                   print("Port {} open".format(port))

                elif result==111:
                   continue

if __name__ == '__main__':
    main()





