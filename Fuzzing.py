import binascii
import threading
# import enchant
import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP
from spellchecker import SpellChecker
from scapy.sendrecv import sniff
from scapy.all import *
import  time


def print_packet(packet):
    spell = SpellChecker()
    t = (bytes)(packet[TCP].payload).decode("utf-8")
    # print(t)
    arr_words=str(t).split(" ")
    a = (map(lambda x: str(x.lower()), arr_words))
    arr_words = list(a)
    # print(arr_words)
    misspelled = spell.unknown(arr_words)
    flag=1
    if len(misspelled)>0:
        print(t)
        print("Fuzzing detected!!!")
        flag= int(input("0 for exit, 1 to continue receiving packets..."))
    else:
        print(t)
    # print("You have", len(misspelled), "unknown words in the msg")
    # for word in misspelled:
    #     print(spell.candidates(word))
    if not flag:
        exit(1)

def capture_sniff():
    sniff(filter="port 22", prn=print_packet)

if __name__=="__main__":
    print("[*] Start sniffing...")
    sniff_thread = threading.Thread(target=capture_sniff())
    sniff_thread.start()
    print("[*] Stop sniffing")
