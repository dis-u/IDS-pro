from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    print(f"Scanning network: {ip_range}")  # Debug print
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    print(f"Devices found: {devices}")  # Debug print
    return devices
