
import socket
import requests

# Get the hostname of the local machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

# Create the URL
url = f"http://{ip_address}:8000"

print(url)
respons=requests.get(url)
print(respons.json())


item = {"key1": "value1", "key2": "value2"}  # Data to be posted as a dictionary

res = requests.post(url, data={"item": item})

print(res.status_code)  # Print the status code of the response
print(res.text)  # Print the response text
print(res)
