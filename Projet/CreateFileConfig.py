import sys
import re
from Interface import *
from Scan import *

#-*- coding: utf-8 -*-

class Config:
    def find_addr(self,filepath):
        
        try:
             file_config = open(filepath, 'r')
             print(file_config)
        except:
             print("no such file!")
             sys.exit(1)
             
        list_content = []
          #read all the text and add in the list
        for i in file_config.readlines():
            list_content.append(i)
        #print(list_content)
        file_config.close()
        for i in range(len(list_content)):
            if "remote" in list_content[i]:
                
                ip = list_content[i].split(" ")
                
                ip = filter(None, ip)
                ip= ip[1]
                  
        return ip


c= Config()

def ConFile(filepath,ip,port):
    content = ''
    list_content = []
    fileConfig = open(filepath, 'r')
    #read all the test and add in the list
    for i in fileConfig.readlines():
            list_content.append(i)
    fileConfig.close()

    for i in list_content:
        if(i.find('remote '+ ip) >= 0):
                i = 'remote ' + ip +" "+ str(port) + '\n'
        content = content + i
    try:
        open(filepath, 'w').writelines(content)
            
    except:
        sys.exit(1)
    print 'ConfigFile changed with succes'

def ChangeLogin(filepath,Login,Password):
    content = ''
    list_content = []
    fileConfig = open(filepath, 'r')
    #read all the text and add in the list
    for i in fileConfig.readlines():
            list_content.append(i)
    fileConfig.close()

    for i in list_content:
        if(i.find('auth') >= 0):
            print 'Begin'
            
    for i in list_content:
        if(i.find('auth') >= 0):
                i = 'auth-'+Login+'-'+Password+' test-vpn@vpn.fdn.fr test '+'\n'
        content = content + i
    try:
        open(filepath, 'w').writelines(content)
            
    except:
        sys.exit(1)
    print 'Login & Password changed with succes'


def ChangeServer(filepath,ip):
    content = ''
    list_content = []
    fileConfig = open(filepath, 'r')
    #read all the text and add in the list
    for i in fileConfig.readlines():
            list_content.append(i)
    fileConfig.close()

    for i in list_content:
        if(i.find('remote ') >= 0):
                i = 'remote ' + str(ip) + " 1194" +'\n'
        content = content + i
    try:
        open(filepath, 'w').writelines(content)
            
    except:
        sys.exit(1)
    print 'ServerName changed with succes'
    
def ChangeProto(filepath,proto):
    content = ''
    list_content = []
    fileConfig = open(filepath, 'r')
    #read all the text and add in the list
    for i in fileConfig.readlines():
            list_content.append(i)
    fileConfig.close()

    for i in list_content:
        if(i.find('proto ') >= 0):
            if(i.find('#proto ') < 0):    
                i = 'proto ' + str(proto) +'\n'
        content = content + i
    try:
        open(filepath, 'w').writelines(content)
            
    except:
        sys.exit(1)
    print 'Proto changed with succes'
    
def ChangeCertificat(filepath,certificat):
    content = ''
    list_content = []
    fileConfig = open(filepath, 'r')
    #read all the text and add in the list
    for i in fileConfig.readlines():
            list_content.append(i)
    fileConfig.close()

    for i in list_content:
        j=i
        if(i.find('<ca>') >= 0):
            print 'Begin'
            
            for j in list_content:
                if(j.find('</ca>') >= 0):
                    print 'END'
                    break
                else:
                    j = '<ca>' + '\n' + certificat + '\n' + '</ca>' + '\n'
            
        content = content + str(j)
        
        try:
            open(filepath, 'w').writelines(content)
        except:
            sys.exit(1)
                    
    print 'Certificat changed with succes'
s = scan()

def lanch(filepath):
    
    ip = c.find_addr(filepath)

    port = PortScanManager(ip)

    proto = s.getProto()
    ChangeProto(filepath,proto)
    ConFile(filepath,ip,port)
    
    
    return ip
