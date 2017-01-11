#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
from socket import *
import  time
from Queue import Queue
import threading
import random
import os
import sys


list = [80 ,443, 8080, 20, 21, 22, 23, 992, 25, 587, 465, 119, 563, 43, 53, 110, 995, 143, 220, 993, 554, 7, 8, 9, 67, 68, 137, 138, 139, 1023, 1024, 1025, 1194, 3690, 3724, 4155, 4242, 4662, 5060, 5061, 5222, 5223, 5269, 5280, 6666, 6667, 6668, 6697, 6969, 8000, 9418]
#for changing place of ports in list
random.shuffle(list)
BUFFER_SIZE=2048

list2 = [1]
lport = []
NumberThread = 20


# The Class scan containt all function of scan Ports
class scan:
    bool = 0
    list2 = []
    exitC = 0
    tcp = 0
    udp = 0

#geters and seters
    def getProto(self):
        return scan.proto

    def setProto(self, proto):
        scan.proto = proto

    def getX(self):
        return scan.exitC
        
    def getList2(self):
        return scan.list2
    
    def setList2(self, list2):
        scan.list2 = list2
    
    def getIp(self):
        return scan.ip
    
    def setIp(self, ip):
        scan.ip = ip


    def getBool(self):
        return scan.bool

    def setBool(self, bool):
        scan.Bool = bool

    def geTtcp(self):
        return scan.tcp
    def geTudp(self):
        return scan.udp

    def setUdp(self, udp):
        scan.udp = udp

    def setTcp(self, tcp):
        scan.tcp = tcp

    def setX(self, x):
        scan.exitC = x

#this is a semaphore
    Lock = threading.Lock()

#this is a fntion for scan TCP ports OF an VPN server

    def TcpScan(self,ip,port):
            tcp = 1
            print ('TCP scanning port',port)
            s = socket(AF_INET, SOCK_STREAM)
            try:
#initiaite connexion  if it works add add list to open ports list
                s.connect((ip, port))
                s.settimeout(1)
                scan.Lock.acquire()
                print "TCP Port %d: is OPEN <<<----------------------->>>"%port
                scan.setTcp(self,1)
                lport.append(port)
                scan.Lock.release()
                scan.setProto(self,'tcp')
#else
            except :

                scan.Lock.acquire()
                print "TCP Port %d is CLOSED" % port
                scan.setProto(self,'tcp')

                scan.Lock.release()

#close connexion
            s.close()

# this is a function wich are used to scan aquilnet server and test if port and open then if it is not a porxy server

    def TcpScanWithAquilonet (self,ip,port):

            tcp = 1

            print ('TCP scanning port',port)
#tcp socket
            s = socket(AF_INET, SOCK_STREAM)
            try:
                message = 'message'
                s.connect((ip, port))
                s.send(message)
                print ('donne envoyer en tcp est ',message)
                data = s.recv(BUFFER_SIZE)
                print ('data recu est ',data)
                s.settimeout(1)
#if data send and receved is the same
                if (message == data ):
                    print (message == data)
                    scan.Lock.acquire()
                    print "TCP Port %d: is OPEN <<<----------------------->>>"%port
                    scan.setTcp(self,1)
                    lport.append(port)
                    scan.setProto(self,'tcp')

                    scan.Lock.release()
                else  :
                    print ('il y a un porxy qui tourne sur ce port')


            except :

                scan.Lock.acquire()
                print "TCP Port %d is CLOSED" % port
                scan.Lock.release()

            s.close()

#this function scan udp port of an vpn server whterver domaine name of server

    def PortScanUdp(self,ip,port):

                sock = socket(AF_INET, SOCK_DGRAM) # open a new socket UDP
                BUFFER_SIZE = 2048#buuffer
                data = (' 38 36 d9 fc 5f e3 fe f7 09 00 00 00 00 ')#captured data send
                datalist = data.split(" ") #conversion of data
                data_s = ''.join(datalist).decode('hex')#data  converted
                semaphore = threading.Lock()

                print ('                              ')
                print ('******************************')
                print ('                              ')
                print("UDP SCAN OF SERVER :", ip)
                print("UDP SCANN OF PORT :", port)
                print ('******************************')
                sock.connect((ip, port))
                sock.send(data_s)
                sock.settimeout(2)

                try :
                        print("REPONSE DU SERVER data reccu ",sock.recvfrom(BUFFER_SIZE))
                        list.append(port)

                        print("PORT IS OPEN !!!!!!!!!!!!!!!!!!!!!!!!!!!!",port)
                        scan.setUdp(self,1)
                        scan.setBool(self,1)
                        lport.append(port)
                        scan.setProto(self,'udp')



                except timeout :


                       print ('Port is closed' ,port)
                       sock.close()



# this is a function wich are used to  aquilnet server and test if port and open then if it is not a porxy server

    def PortScanUdpWithAquilonet(self,ip,port):
                sock = socket(AF_INET, SOCK_DGRAM) # open a new socket UDP
                BUFFER_SIZE = 2048
                data = ('38 36 d9 fc 5f e3 fe f7 09 00 00 00 00')
                datalist = data.split(" ")
                data_s = ''.join(datalist).decode('hex')
                print ("data ENVOYER EST ",data_s)
                semaphore = threading.Lock()

                print ('                              ')
                print ('******************************')
                print ('                              ')
                print("UDP SCAN OF SERVER :", ip)
                print("UDP SCANN OF PORT :", port)
                print ('******************************')
                sock.connect((ip, port))
                sock.send(data_s)
                sock.settimeout(2)
                try :
                        datarecu,a = sock.recvfrom(BUFFER_SIZE)


                        print("REPONSE DU SERVER data reccu ",datarecu)

                        if ( datarecu == data_s ):

                            list.append(port)
                            print("PORT IS OPEN !!!!!!!!!!!!!!!!!!!!!!!!!!!!",port)
                            scan.setUdp(self,1)
                            scan.setBool(self,1)
                            lport.append(port)
                            scan.setProto(self,'udp')



                except timeout :


                       print ('Port is closed' ,port)
                       sock.close()
    

    def ReadList2(self):
            #Read the file port_list for level2
        if os.path.exists('port_list.txt') :
            print("port_list file exsit")
            pass
        else:
                #if no file creat new file
            print("file no exsit,and creat file")
            f = open('port_list.txt', 'w')
            f.close()
                    
        port_list = open('port_list.txt','r')
        list0=[]
                                    
        for i in port_list.readlines():                
            list0.append(i)
                    
        if len(list0 ) > 0: 
            print("port_list file null")                
            list0=map(int,list0)
            list2=list0
            sc.setList2(list2)
        return self.list2

    def PortList2(self):
        #If we find in niveux 3 and we add in the file which contain the port list for level2 
        if os.path.exists('port_list.txt') :
            print("file exsit")
            pass
        else:
            #if no file creat new file
            print("file no exsit,creat file")
            f = open('port_list.txt', 'w')
            f.close()
                    
        addport=str(lport[0]) 
        port_list = open('port_list.txt','r')
        list1=[]
        for i in port_list.readlines():
            list1.append(i)
        j = 0
        bool_port =0 
        while j < len(list1):
            print(list1[j])
            if addport in list1[j]:
                bool_port=1
                break
            j+=1
        if bool_port==1 :
            print("same port in the list")
            pass
        else:
            open('port_list.txt','a').write(addport+'\n')
            print("port add in the file port_list")
            print("lport:",addport)
        port_list.close()


sc = scan()

# this function fun thread which are in Qeue , it run PortScanUdpWithAquilonet and TcpScanWithAquilonet
def threader():
    while True and sc.getBool() == False:
      if sc.exitC== 0 :
        worker = q.get()
        sc.PortScanUdpWithAquilonet(sc.getIp(),worker)
        # completed with the job
        q.task_done()
      else:
        worker = q2.get()
        sc.TcpScanWithAquilonet(sc.getIp(),worker)
        # completed with the job
        q2.task_done()

#waiting thread list of threads
q = Queue(NumberThread)


#waiting thread list of threads
q2= Queue(NumberThread)

#PortScanManger this is a manager of our scan it run scans of level 1 list UDP scan ten TCP scan

def PortScanManager(ip):

#Get IP ADRESS OF VPN SERVER FROM OPENVPN CONFIG
        ip = 'neutral-echo.aquilenet.fr'
        sc.setIp(ip)

        print ('----------------------------')

        print ('Welcome we will scan ports ',ip)
        print ('----------------------------')


# scan UDP of list of first level ports using threads



        print ('Scan First Level List UDP')

        for x in range(NumberThread):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()
        worker0=0
#cheeek if we found a open port we stop put threads in Queue and stop other treads

        while worker0 < len(list) and sc.geTudp()==0:
                      q.put(list[worker0])
                      worker0 = worker0+1
        for worker0 in range(len(list)):
                      q.join()


# scan TCP of list of first level ports using threads


        if sc.geTudp()== 0 :
            print ('----------------------------')
            print ('Scan First Level List TCP')
            print ('----------------------------')

            for x in range(NumberThread):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()
            worker0=0
#cheeek if we found a open port we stop put threads in Queue and stop other treads

            while worker0 < len(list) and sc.geTtcp()==0:
                      q.put(list[worker0])
                      worker0 = worker0+1
            for worker0 in range(len(list)):
                      q.join()


# scan UDP of list of second level ports using threads


        if sc.geTudp()==0 and sc.geTtcp()==0 and len(list2) > 0:

            print ('Scan second Level List UDP')
            sc.ReadList2()

            for x in range(NumberThread):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()
            worker0=0
            #cheeek if we found a open port we stop put threads in Queue and stop other treads

            while worker0 < len(list2) and sc.geTudp()==0:
                      q.put(list2[worker0])
                      worker0 = worker0+1
            for worker0 in range(len(list2)):
                      q.join()


# scan TCP of list of second level ports using threads

        if sc.geTudp()==0 and sc.geTtcp()==0 and len(list2):
            print ('----------------------------')
            print ('Scan second Level List TCP')
            print ('----------------------------')
            sc.ReadList2()

            for x in range(NumberThread):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()
            worker0=0
#cheeek if we found a open port we stop put threads in Queue and stop other treads
            while worker0 < len(list2) and sc.geTudp()==0:
                      q.put(list2[worker0])
                      worker0 = worker0+1
            for worker0 in range(len(list2)):
                      q.join()


#        Scan  UDP WITH THREAD ALL PORTS



        if sc.geTudp()==0 and sc.geTtcp()==0:
            print ('Scan All of List 1-65535 Level List UDP THREAD')
            print ('----------------------------')

            for x in range(NumberThread):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()
            worker0=1
            while worker0 < 65000 and sc.geTudp()==0:
                      q.put(worker0)
                      worker0 = worker0+1
            for worker0 in range(len(list)):
                      q.join()
            sc.PortList2()






# Scan  TCP WITH THREAD ALL PORTS

        if sc.geTudp()==0 and sc.geTtcp()==0:
            sc.setX(1)

            print ('Scan All of List 1-65535 Level List TCP THREAD')
            print ('----------------------------')
            for x in range(20):
                   t = threading.Thread(target=threader)
                   t.daemon = True
                   t.start()

            worker0=0
            c=0

            while worker0 < 65535 and sc.geTtcp()==0:
                      q2.put(worker0)
                      worker0=  worker0+1

            for worker0 in range(len(list)):
                      q2.join()
            sc.PortList2()

        print ("fin de tout les threads tcp")
        print ("**************************************Port ",lport)
        
        return lport[0]
