from scapy.all import sniff, get_if_list
import requests

flask_server = "http://192.168.86.92:5000"

# List available network interfaces
print("Available Network Interfaces:")
interfaces = get_if_list()
for iface in interfaces:
    print(iface)

INTERFACE = "\\Device\\NPF_{A670E03B-97B4-403C-9444-FC223AF9698A}"
print("Script started... Monitoring network traffic on:", INTERFACE)

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        
        # Detect port scanning (SYN flag check)
        if packet.haslayer("TCP") and packet["TCP"].flags == 2:  # SYN packet
            alert_msg = f"PortScan_from_{src_ip}"
            print(f"[ALERT] Port scan detected from {src_ip}")
            requests.get(f"{flask_server}/add_alert/{alert_msg}")

        # Detect traffic from blacklisted IPs
        blacklist = ["192.168.1.105", "10.10.10.200"]
        if src_ip in blacklist:
            alert_msg = f"MaliciousTraffic_from_{src_ip}"
            print(f"[ALERT] Malicious traffic detected from {src_ip}")
            requests.get(f"{flask_server}/add_alert/{alert_msg}")

            # Choose the correct interface manually

sniff(iface=INTERFACE, prn=packet_callback, store=0)


# Start sniffing packets
sniff(iface=INTERFACE, prn=packet_callback, store=0)

def packet_callback(packet):
    print(packet.summary())  # Debugging: Show all packets
