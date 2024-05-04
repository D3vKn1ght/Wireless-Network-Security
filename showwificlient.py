from scapy.all import *
import subprocess

conf.iface = "wlp0s20f3mon"

interface = input(f"Nhập interface mạng được thiết lập monitor mode ({conf.iface}): ").strip() or conf.iface

networks = {}
clients = {}

def change_channel():
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        ch = ch % 12 + 1
        time.sleep(1)

def handle_packet(packet):
    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        bssid = packet[Dot11].addr2.upper()
        ssid = packet.info.decode() if packet.info else b''
        if bssid not in networks:
            networks[bssid] = ssid
            print(f"SSID: {ssid}, BSSID: {bssid}")

    elif packet.haslayer(Dot11) and packet.type == 2 and not packet.haslayer(EAPOL):
        client = packet[Dot11].addr2.upper()
        bssid = packet[Dot11].addr1.upper()

        if bssid in networks:
            ssid = networks[bssid]
            if client not in clients or (client in clients and bssid != clients[client]["bssid"]):
                clients[client] = {'bssid': bssid, 'ssid': ssid}
                print(f"Client {client} connected to BSSID {bssid} (SSID: {ssid})")

if __name__ == "__main__":
    interface_run = conf.iface.rstrip("mon")
    subprocess.call(["airmon-ng", "start", interface_run])
    
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()
    
    sniff(prn=handle_packet, iface=interface, monitor=True)
