from scapy.layers.inet import IP, TCP
from scapy.all import *
import  time


def capture_summary():
    for i in range(10):
        # send(IP(dst=['10.0.0.138']) / TCP(dport=22)/"Hello World")
        # send(IP(dst=['10.0.0.138']) / TCP(dport=22)/("0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, ").encode("utf-8"))
        time.sleep(5)


capture_summary()