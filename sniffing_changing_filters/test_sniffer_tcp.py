#!/usr/bin/env python3
from scapy.all import*
a=IP(src='10.0.2.4',dst='8.8.8.8')/TCP(dport=23)
send(a)
