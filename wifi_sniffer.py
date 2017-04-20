# Offensive Security Software
# SSE Program
# Attack: Wifi Sniffer
# Date: February 2, 2016
# Description: Passively reads the network traffic and in the best case,
# evaluates data and beacon frames to extract information like SSID, channel,
# and client IPs/MACs

import os
from scapy.all import *

iface = "en0"

os.system("/usr/sbin/ifconfig " + iface + " mode monitor")

#Dump packets that are not beacons, probe request / responses
def dump_packet(pkt):
    if not pkt.haslayer(Dot11Beacon) and \
       not pkt.haslayer(Dot11ProbReq) and \
       not pkt.haslayer(Dot11ProbResp):
        print pkt.summary()

        if pkt.haslayer(Raw):
            print hexdump(pkt.load)
            print "\n"


while True:
    for channel in range(1, 14):
        os.system("ifconfig " + iface + " channel " + str(channel))
        print "Sniffing on channel " + str(channel)

        sniff(iface=iface, prn=dump_packet, count=10, timeout=3, store=0)


