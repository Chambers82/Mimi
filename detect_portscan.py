# Offensive Security Software
# SSE Program
# Attack: Port Scan Detector
# Date: January 31, 2016

import sys
from time import time
from scapy.all import sniff

ip_to_ports = dict()

#Nr of ports in timespan seconds
nr_of_diff_ports = 10
portscan_timespan = 10

def detect_portscan(packet):
    ip = packet.getlayer("IP")

    tcp = packet.getlayer("TCP")

    #Remember scanned port and time in unix format
    ip_to_ports.setdefault(ip.src, {}) \
        [str(tcp.dport)] = int(time())

    #Source IP has scanned too many different ports?
    if len(ip_to_ports[ip.src]) >= nr_of_diff_ports:
        scanned_ports = ip_to_ports[ip.src].items()

        #Check recorded time of each scan
        for (scanned_port, scan_time) in scanned_ports:

            # Scanned port not in timeout span? Delete it
            if scan_time + portscan_timespan < int(time()):
                del ip_to_ports[ip.src][scanned_port]

        # Still too much scanned ports?
        if len(ip_to_ports[ip.src]) >= nr_of_diff_ports:
            print "Portscan detected from " + ip.src
            print "Scanned ports " + \
                  ",".join(ip_to_ports[ip.src].keys()) + \
                  "\n"

            del ip_to_ports[ip.src]

if len(sys.argv) < 2:
    print sys.argv[0] + " <iface>"
    sys.exit(0)

sniff(prn=detect_portscan,
      filter="tcp",
      iface=sys.argv[1],
      store=0)


#To block with iptables
# os.system("iptables -A INPUT -s " + ip_to_ports[ip.src] + " -j DROP")

