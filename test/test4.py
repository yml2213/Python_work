import json
from urllib import parse

dict = {"area": "市中区", "city": "济南市", "mobid": "e998cb31be347dc0", "opentype": 0, "password": "zgxw123456",
        "province": "山东省", "sex": 0, "source": "12-Xiaomi M2102J2SC-2.5.0", "userid": "0", "username": "15339956683"}
s = json.dumps(dict)
print(s)

a = parse.quote_plus(s)
print(a)
