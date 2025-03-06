import requests

base_url = "http://192.168.86.92:5000"

# Add test alerts
requests.get(f"{base_url}/add_alert/UnauthorizedAccess")
requests.get(f"{base_url}/add_alert/PortScanDetected")
requests.get(f"{base_url}/add_alert/MalwareSignatureFound")

# Fetch alerts
response = requests.get(f"{base_url}/alerts")
print("Current Alerts:", response.json())  # Verify alerts in console
