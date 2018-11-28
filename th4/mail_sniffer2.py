from scapy.all import *

def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet=str(packet.[TCP].payload)
        if 'user' in mail_packet.lower() or 'pass' in mail_packet.lower():
            print("[*]Server: {} ".format(packet[IP].dst))
            print("[*] {}".format(packet[TCP].payload))
sniff(filter='tcp port 110 or tcp port 25 tcp port 141',prn=packet_callback,store=0)
