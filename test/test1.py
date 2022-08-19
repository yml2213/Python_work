<<<<<<< HEAD
import requests

url = "https://wprophecy.com/user/appuser/info"

payload = {}
headers = {
    'cookie': 'WAR_PROPHECY=s%3As7zP1akNZl1BDontoOFunmi9NCW5guAL.V5xaTRxFh8tu9PhnXicqiDCUXQTCcOrvX6rm6CF6qPI; REM_TOKEN=W0YkTBijxlRyjojNT6QyOWXubaMx0u4nwiX54Bs4t2kU4RLNKigPio9LxG5rr9eH; WAR_PROPHECY=s%3AUvZwdX7eUNVcPYeMmvjIw64pchwcFxtg.A%2FQ3XgEG%2B%2FL9xsdw9F53xLX5LKH0cnTJCrqphqcHu%2FQ'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.headers['Set-Cookie'])
=======
import binascii
from urllib import parse

from pyDes import des, CBC, PAD_PKCS5

# 秘钥
KEY = 'ZG#)@F01'


def md5_encrypt(_data):
    import hashlib
    md5 = hashlib.md5()
    md5.update(_data.encode(encoding='utf-8'))
    return md5.hexdigest()


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()


a = {"area": "市中区", "city": "济南市", "mobid": "e998cb31be347dc0", "opentype": 0, "password": "zgxw123456",
     "province": "山东省", "sex": 0, "source": "12-XiaomiM2102J2SC-2.5.0", "userid": "0", "username": "15339956683"}

newdict2 = str(a)
strdict3 = newdict2.replace("\'", "\"")
strdict4 = strdict3.replace(" ", "")
a = parse.quote_plus(strdict4)
# print(a)
Params_data = des_encrypt(a)
Params_data = str.upper(Params_data)
print(Params_data)

sign_data = f'ZG#)@F01Methoduservip.member.loginParams{Params_data}ZG#)@F01'
sign = md5_encrypt(sign_data)
print("==========================")
print(sign)
>>>>>>> 4d38f36f9d954872f09e9ad3a018638c73d5113e
