import binascii
import threading

import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP

from scapy.sendrecv import sniff
from scapy.all import *
import  time
# while(1):
#     capture = sniff()
#     # capture = sniff(filter="port 22")
#     for l in capture:
#         print(l)
#     time.sleep(5)
# global capture
# def capture_sniff():
#     global capture
#     # capture = sniff(filter="port 22")
#     capture = sniff()
#
# def capture_summary():
#     global capture
#     capture.summary()
#
# sniff_thread = threading.Thread(target=capture_sniff())
# print_thread = threading.Thread(target=capture_summary())
# sniff_thread.start()
# print_thread.start()
# packet=sniff(prn=lambda x:x.summary())

def print_packet(packet):
    # if packet.haslayer(IP):
    #     ip_layer = packet.getlayer(IP)
    #     if ip_layer.haslayer(TCP):
    #         tcp_udp_layer= ip_layer.getlayer(TCP)
    #         if tcp_udp_layer.haslayer('SSH'):
    #             pkt_str = packet.show(dump=True)
    #             print(pkt_str)
    #     elif ip_layer.haslayer(UDP):
    #         tcp_udp_layer= ip_layer.getlayer(UDP)
    #         if tcp_udp_layer.haslayer('SSH'):
    #             pkt_str = packet.show(dump=True)
    #             print(pkt_str)
    pkt_str = packet.show(dump=True)
    # pkt = binascii.hexlify(bytes(packet[TCP].payload))
    # print(pkt)
    # print(packet)
    # print(pkt_str)
    t = packet[TCP].payload
    types=[str,int,float,complex, list , tuple , range, dict,set, frozenset,bool,bytes, bytearray, memoryview]
    if type(t) not in types:
        print("NOT")
    t2= (bytes(t)).decode("utf-8")
    if t2=="":
        print ("EXIT")
    else:
        print(t2)
    # print(binascii.hexlify(t))



def capture_sniff():
    sniff(filter="port 22", prn=print_packet)

def capture_summary():
    for i in range(10):
        send(IP(dst=['10.0.0.138']) / TCP(dport=22, flags='S'))
        time.sleep(3)

print("[*] Start sniffing...")
sniff_thread = threading.Thread(target=capture_sniff())
# print_thread = threading.Thread(target=capture_summary())
# print_thread.start()
sniff_thread.start()
print("[*] Stop sniffing")
