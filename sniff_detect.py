# Offensive Security Software
# SSE Program
# Attack: Sniff Detection
# Date: January 31, 2016

import sys
from scapy.all import promiscping

if len(sys.argv) < 2:
    print sys.argv[0] + " <net>"
    sys.exit()

promiscping(sys.argv[1])
