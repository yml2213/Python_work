import os

import requests

if not os.path.exists("sendNotify.py"):
    try:
        url = 'https://raw.gh.fakev.cn/yml2213/Python/master/sendNotify.py'
        response = requests.get(url)
        with open('sendNotify.py', "w+", encoding="utf-8") as f:
            f.write(response.text)
    except Exception as e:
        print(e)
else:
    print("文件已存在,跳过")
    pass
