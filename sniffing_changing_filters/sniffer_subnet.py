#!/usr/bin/env python3
from scapy.all import*
def print_pkt(pkt):
	pkt.show()
pkt = sniff(iface='enp0s3', filter='net 8.8.8.0/24', prn=print_pkt)
