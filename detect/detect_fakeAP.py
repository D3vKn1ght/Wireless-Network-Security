from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ap_mac = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        print(f"AP MAC: {ap_mac} with SSID: {ssid}")

sniff( prn=packet_handler, store=0)
