import requests
url="https://www.1point3acres.com/bbs/thread-927931-1-1.html"
response = requests.get(url)
print(response.text)