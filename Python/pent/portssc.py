import sys
import socket as ck
import pyfiglet as pf

ascii_banner = pf.figlet_format("TryHackMe \n Python 4 Pents \n ScannyBoi")
print(ascii_banner)

ip = 'ANY-IP'
open_ports = []

ports = range(1, 65535)

def probe_port(ip, port, result = 1):
    try:
        sock = ck.socket(ck.AF_INET, ck.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result
for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)
if open_ports:
    print("Open Ports are: ")
    print(sorted(open_ports))
else:
    print("No open ports...")