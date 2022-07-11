import os

import requests


def getsendNotify(self, a=0):
    name = "sendNotify.py"
    os.path.isfile(name)
    
    if a == 0:
        a += 1
    try:
        url = 'https://raw.gh.fakev.cn/yml2213/Python/master/sendNotify.py'
        response = requests.get(url)
        if 'curtinlv' in response.text:
            with open('sendNotify.py', "w+", encoding="utf-8") as f:
                f.write(response.text)
        else:
            if a < 5:
                a += 1
                return self.getsendNotify(a)
            else:
                pass
    except:
        if a < 5:
            a += 1
            return self.getsendNotify(a)
        else:
            pass


a = 1
getsendNotify(a)
