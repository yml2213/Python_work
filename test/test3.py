import requests

url = "https://wprophecy.com/betting/create"

payload = 'amountNoWar=100&roundId=254'
headers = {
    'Cookie': 'WAR_PROPHECY=s%3Ac4tjIh069kHAmjjP1Qd-vGJFo5R26ITz.ZUX8%2FwS9jXDHH%2FKCk%2BpHNSAZReAZyUqhW%2BwCv1VvCtQ; REM_TOKEN=A66qoKmzgjmNhulRt6yanp2DRcdYWX72fSAjkP6v8ZhGc0sa8KiYEp89j1A5jaXV',
    'CSRF-TOKEN': 'QFGKX55g-np9BqMKc5zVjv1rP7rU-WGm9nn4',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
