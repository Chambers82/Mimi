# Offensive Security Software
# SSE Program
# Attack: Wifi Hidden SSID Retrival
# Date: February 1, 2016
# Description: Hidden SSID's only avoid adding the SSID to beacon frames.  These
# probes and the network itself can be seen, it's only the SSID is not broadcast.
# This script will read all packets and dump the SSID if it can find it.

from scapy.all import *

iface = "en0"

#Print the SSID of probe requests, probe response, or association request

def handle_packet(packet):
    if packet.haslayer(Dot11ProbReq) or \
       packet.haslayer(Dot11ProbResp) or \
       packet.haslayer(Dot11AssoReq):
        print "Found SSID " + packet.info

# Put device into monitor mode
os.system("ifconfig " + iface + " mode monitor")

#Sniff Sniff
print "Sniffing on interface " + iface
sniff(iface=iface, prn=handle_packet)


#The "Security feature" of hiding SSID's is only effective if no clients
# are connected to the "hidden" network.  Hack the planet.

