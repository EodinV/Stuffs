from scapy.all import *

interface = "wlan0"
ip_range = "10.10.30.160/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout = 2, iface = interface, inter = 0.1)

for send, recieve in ans:
    print(receive.sprintf("%Ether.src% - %ARP.psrc%"))