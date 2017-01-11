from CreateFileConfig import *
from Interface import *

test = 'certificat'
filepath ="ConfigFile.ovpn"
ChangeCertificat(filepath,test)

def comparaison(filepath):    
        content = ''
        list_content = []
        fileConfig = open(filepath, 'r')
        for i in fileConfig.readlines():
                list_content.append(i)
        fileConfig.close()

        for i in list_content:
            j=i
            if(i.find('<ca>') >= 0):
                
                for j in list_content:
                    if(j.find('</ca>') >= 0): # this is the problem
                        
                        break
                    else:
                        j = test 
                
            content = content + str(j)

        if content == test :
            
            print "test with succes"

        else:
            print "ERROR !"
            

comparaison(filepath)
            



