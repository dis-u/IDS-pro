import numpy as np

traffic_history = []

def anomaly_based_detection(packet):
    global traffic_history
    traffic_history.append(packet["length"])

    if len(traffic_history) > 100:
        avg_traffic = np.mean(traffic_history[-100:])
        std_dev = np.std(traffic_history[-100:])
        
        if packet["length"] > avg_traffic + (3 * std_dev):
            print(f"🚨 Anomaly Detected! Large Packet from {packet['src_ip']}")
