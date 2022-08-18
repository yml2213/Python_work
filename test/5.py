import requests

url = "https://wprophecy.com/getCSRFToken"

payload = {}
headers = {
    'cookie': 'REM_TOKEN=W0YkTBijxlRyjojNT6QyOWXubaMx0u4nwiX54Bs4t2kU4RLNKigPio9LxG5rr9eH',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.cookies)
