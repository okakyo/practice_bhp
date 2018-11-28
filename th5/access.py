import requests

body=requests.get('https://www.google.com')
print(body.headers)
