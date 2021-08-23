#!/usr/bin/python3
'''
Raw scanner written in python 3 by Mattia Campagnano on Tue 10 Aug 2021 10:46:09 PM EDT.
It reads a list of IP addresses from a text file, loops through them
and, for each IP, it connects to ports 1 thru 65,535 returning a message
if the port is open

'''

import socket
import sys
import threading
from queue import Queue


# Grab target IP addresses from a file, whose filepath is passed as an argument.
file=sys.argv[1]

# Loop through ports 1 thru 65,535.  
      
for port in range(1,65535): 

# Open input file, read it, loop through each target IPs

    with open(file,'r') as f:

         for line in f:
              ip_addr=line.strip()

# Create a network socket
              s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              socket.setdefaulttimeout(1)
              print_lock = threading.Lock()

# Try connecting to each target IPs on ports 1 thru 65,535

              result = s.connect_ex((ip_addr,port))
              
# If the connection returns no error, then the port is open

              if result ==0:
                   print("Port {} is open for ip {}".format(port, ip_addr))

# Function handling threads

def threader():
   while True:

# get worker from queue
      worker = q.get()
      
      
      q.task_done()

q = Queue()

for x in range(200):
   
   t = threading.Thread(target = threader)
   
   
   t.daemon = True
   
# Start threads
   t.start()
 
# Range or variable passed to the worker pool   
for worker in range(1, 65535):
   q.put(worker)
 
# Wait until thread terminates   
q.join()
 
# Close network socket

s.close()
sys.exit()


