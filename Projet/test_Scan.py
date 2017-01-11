from Scan import *


Port = PortScanManager("vpn2-rw.fdn.fr")

if Port == "1194" :
    print "Scan with succes"
else:
    print "ERROR !"
