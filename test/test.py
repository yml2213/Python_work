import requests

url = "https://raw.gh.fakev.cn/yml2213/Python/master/ceshi/ceshi.py"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
