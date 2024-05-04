from scapy.all import *

mac_to_ssid = {}

def handle_packet(packet):
    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        ssid = packet[Dot11Elt].info.decode()
        mac_address = packet[Dot11].addr2
        mac_to_ssid[mac_address] = ssid
    elif packet.haslayer(Dot11Deauth):
        sender = packet[Dot11].addr2
        receiver = packet[Dot11].addr1
        ssid = mac_to_ssid.get(sender, "Unknown SSID")
        print(f"Deauth detected from {sender} to {receiver}, SSID: {ssid}")

interface = "wlp0s20f3mon"
print("Detecting deauthentication attacks...")
sniff(iface=interface, prn=handle_packet, store=False)
