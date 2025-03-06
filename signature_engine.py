import json

def load_rules():
    with open('rules.json') as f:
        return json.load(f)["rules"]

def signature_based_detection(packet):
    rules = load_rules()
    
    for rule in rules:
        if rule["attack"] == "Port Scan" and packet["protocol"] == 6:  # TCP
            print(f"🚨 Port Scan Detected from {packet['src_ip']}!")

if __name__ == "__main__":
    test_packet = {"src_ip": "192.168.1.1", "dst_ip": "192.168.1.10", "protocol": 6, "length": 100}
    signature_based_detection(test_packet)
