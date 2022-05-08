import random
from scapy.layers.inet import IP, TCP
from scapy.all import *
import time

msg_for_atck=["I love you", "xxxxxxx", "kaka hara atkafa", "hello world", "shhh ya barbari",
              "geeks for geeks", "King David of Israel", "bopuryr", "hrgiltrh ghlwruihgiu gerhgi grugh",
              "Israel forever", "puta madrid", "Haifa"]
def capture_summary():
    time.sleep(5)
    my_msg_index= random.randint(0,len(msg_for_atck)-1)
    my_msg=msg_for_atck[my_msg_index]
    send(IP(dst=['10.0.0.138']) / TCP(dport=22)/my_msg)

if __name__=="__main__":
    for i in range(7):
        capture_summary()