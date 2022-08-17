import requests

url = "https://wprophecy.com/user/appuser/info"

payload = {}
headers = {
    'cookie': 'WAR_PROPHECY=s%3As7zP1akNZl1BDontoOFunmi9NCW5guAL.V5xaTRxFh8tu9PhnXicqiDCUXQTCcOrvX6rm6CF6qPI; REM_TOKEN=W0YkTBijxlRyjojNT6QyOWXubaMx0u4nwiX54Bs4t2kU4RLNKigPio9LxG5rr9eH; WAR_PROPHECY=s%3AUvZwdX7eUNVcPYeMmvjIw64pchwcFxtg.A%2FQ3XgEG%2B%2FL9xsdw9F53xLX5LKH0cnTJCrqphqcHu%2FQ'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.headers['Set-Cookie'])
