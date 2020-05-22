import requests
req = requests.get('https://tutsplus.com/')

print(req.encoding)
print(req.status_code)