
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

respons2=requests.post(url,item=10)
print(respons2)
