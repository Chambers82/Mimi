# Offensive Security Software
# SSE Program
# Main Index Module and Interface (MIMI)
# Filename mimi_ui.py
# Date February 1, 2016
# Description "Banquette Event Order"

import os
import sys
import string

Network_Attacks = [
'ARP Spoofing Over VLAN Hopping',
'ARP-Watcher',
'ARP-Cache Poisoning'
'ARP-Cache Poisoning',
'Automatic TCP Hijack', 
'Cookie Manipulation',
'Deauthenticate User from AP',
'Port Scan Detector',
'DHCP Hijacking',
'DNS Spoofing',
'Spoofing Email Sender',
'HTTP Authentication Sniffing',
'HTTP Directory Scanner',
'HTTP Header Dumper',
'HTTP Referrer Spoofing',
'ICMP Redirector',
'IP Brute Forcer',
'MAC-Flooder',
'Packet Sniffer',
'Port Scanning Through a Proxy',
'HTTP Proxy Scanner',
'Password Sniffer',
'Reverse DNS Scanner',
'RST Daemon',
'SQL Inject (Low Hanging Fruit)',
'SMB Share Scanning',
'Reading and Writing PCAP Dump Files',
'Sniff Detection',
'SQL Inject (Low Hanging Fruit)',
'HTTP/SSL Sniffer',
'SYN-Flooder',
'VLAN Hopping',
'Wifi Hidden SSID Retrival',
'Wifi Prob Request Sniffer',
'WiFi Scanner',
'Wifi Sniffer']


Network_Attacks = {'ARP Spoofing Over VLAN Hopping':'arp-spoof_vlan.py',
'ARP-Watcher':'arp-watcher.py',
'ARP-Cache Poisoning (BiDir)':'arp_cache_bi.py',
'ARP-Cache Poisoning':'arp_poison.py',
'Automatic TCP Hijack':'auto_tcp_hijack.py',
'Cookie Manipulation':'cookie_manip.py',
'Deauthenticate User from AP':'deauth.py',
'Port Scan Detector':'detect_portscan.py',
'DHCP Hijacking':'dhcp_hijack.py',
'DNS Spoofing':'dns_spoof.py',
'Spoofing Email Sender':'email_spoof.py',
'HTTP Authentication Sniffing':'htty_auth_sniff.py',
'HTTP Directory Scanner':'http_dir_scan.py',
'HTTP Header Dumper':'http_header_dump.py',
'HTTP Referrer Spoofing':'http_referer_spoof.py',
'ICMP Redirector':'icmp_redirect.py',
'IP Brute Forcer':'ip_brute_forcer.py',
'MAC-Flooder':'mac-flooder.py',
'Packet Sniffer':'pkt_sniffer.py',
'Port Scanning Through a Proxy':'proxy_port_scan.py',
'HTTP Proxy Scanner':'http_proxy.py',
'Password Sniffer':'pwd_sniffer.py',
'Reverse DNS Scanner':'reverse_dns.py',
'RST Daemon':'rst_daemon.py',
'SMB Share Scanning':'smb_scanner.py',
'Reading and Writing PCAP Dump Files':'sniff2pcap.py',
'Sniff Detection':'sniff_detect.py',
'SQL Inject (Low Hanging Fruit)':'sql_injection.py',
'HTTP/SSL Sniffer':'ssl_sniffer.py',
'SYN-Flooder':'syn-flood.py',
'VLAN Hopping':'vlan_hopper.py',
'Wifi Hidden SSID Retrival':'wifi_find_hidden_ssids.py',
'Wifi Prob Request Sniffer':'wifi_probe_sniffer.py',
'WiFi Scanner':'wifi_scanner.py',
'Wifi Sniffer':'wifi_sniffer.py'}

class Interface:
    Network_Attacks = {}
    attack_dir = "/opt/py/"
    def __init__(self):
        self.Network_Attacks = Network_Attacks
        for item in self.Network_Attacks.keys():
            print item
        print "Main Index Module and Interface console activiated."
        print len(self.Network_Attacks.keys()), "attack modules loaded.\n"
    def list_attacks(self):
        for item in self.Network_Attacks.keys():
            print item
    def list_source_files(self):
        for item in self.Network_Attacks.values():
            print self.attack_dir + item
    def view_source_file(self, filepath):
        file = open(filepath)
        for item in file:
            print item,
    def view_header(self, filepath):
        content = []
        file = open(filepath)
        print "*************************************"
        for item in file:
            if item[0] == "#":
                print item,
        print "*************************************"

    def edit_source(self, filepath):
        os.popen("idle " + filepath)
        


help_file = """
Current Commands
----------------

attacks               Display all loaded attack descriptions
source                Display all loaded attack filepaths
view                  View the source of a supplied module
header                Display the header text of the supplied module
"""


run = Interface()
cmd = raw_input("mimi> ")
while string.upper(cmd) <> "QUIT" or "EXIT":
    cmd = raw_input("mimi> ")
    command = string.split(cmd, " ")
    if string.upper(cmd) == "ATTACKS":
        run.list_attacks()
    elif string.upper(cmd) == "SOURCE":
        run.list_source_files()
    elif string.upper(cmd) == "VIEW":
        print "Usage: view [filename].py"
    elif string.upper(cmd) == "HEADER":
        print "Usage: header [filename].py"
    elif (string.upper(command[0]) == "VIEW" and len(command) >= 2):
        print command[1]
        try:
            run.view_source_file(command[1])
        except:
            print "File not found."
    elif (string.upper(command[0]) == "HEADER" and len(command) >= 2):
        print command[1]
        try:
            run.view_header(command[1])
        except:
            print "File not found."
    elif (string.upper(command[0]) == "EDIT" and len(command) >= 2):
        try:
            run.edit_source(command[1])
        except:
            print "File not found."

    elif (string.upper(command[0]) == "QUIT" or string.upper(command[0]) == "EXIT"):
        print "*********************************************************"
	print "\nMain Index Module and Interface (Mimi) console.  - 2016"
	print "        Copyright 2016 Cocksure Security LLC."
	print "       Support the Free Information Movement.\n"
	print "*********************************************************"
	sys.exit(1)
    elif (string.upper(command[0]) == "HELP"):
        print help_file
    
    else:
        print "Command length: ", len(command)
        print command, ": command not recognized."





