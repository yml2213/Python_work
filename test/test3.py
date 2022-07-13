from urllib import parse

newdict = {"area": "市中区", "city": "济南市", "mobid": "e998cb31be347dc0", "opentype": 0, "password": "zgxw123456",
           "province": "山东省", "sex": 0, "source": "12-Xiaomi M2102J2SC-2.5.0", "userid": "0",
           "username": "15339956683"}  # <class 'dict'>

newdict2 = str(newdict)
strdict3 = newdict2.replace("\'", "\"")
print(type(strdict3))
strdict4 = strdict3.replace(" ", "")
a = parse.quote_plus(strdict4)
print(a)
