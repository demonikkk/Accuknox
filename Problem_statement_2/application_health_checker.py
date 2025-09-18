import requests

URL = "https://example.com"  # Replace with your app URL

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("Application is UP")
    else:
        print(f"Application is DOWN (Status Code: {response.status_code})")
except:
    print("Application is DOWN")
