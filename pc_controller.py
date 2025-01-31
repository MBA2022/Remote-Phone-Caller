import requests

# Replace with your phone's IP address and port
phone_ip = '192.168.0.1'  # Example IP address (replace with your phone's IP)
phone_port = 5000

# Number to call
number_to_call = '+1234567890'  # E.g., '+1234567890'

# Send the request
response = requests.post(
    f'http://{phone_ip}:{phone_port}/call',
    json={'number': number_to_call}
)

print(response.text)