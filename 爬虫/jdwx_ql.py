import os
import re
import time

import requests


def mac_env(name):
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    with open(path, "r+") as f:
        env = f.read()
        if name in env:
            r = re.compile(r'ghxw_data="(.*?)"', re.M | re.S | re.I)
            result = r.findall(env)
            # print(data[0])
            if "@" in result[0]:
                _ck = result[0].split("@")
                ckArr = _ck
            elif "\n" in result[0]:
                _ck = result[0].splitlines()
                ckArr = _ck
            else:
                ckArr = result
        else:
            print(f"检查变量 {name} 是否已填写")


def ql_env(name):
    global ckArr
    if name in os.environ:
        ckArr = []
        _data = os.environ[name]
        if "@" in _data:
            _ck = _data.split("@")
            ckArr = _ck
        elif "\n" in _data:
            _ck = _data.splitlines()
            ckArr = _ck
        else:
            ckArr = _data.split("@")


# 时间戳 转 时间  (2022-07-07 14:51:00)
def ts2time(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp = int(time_stamp * (10 ** (10 - len(str(time_stamp)))))
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


def task_gwc(cookie):
    # 购物车
    url_gwc = "https://lzkjdz-isv.isvjd.com/wxAssemblePage/queryActInfo"

    payload = "pageNo=1&pageSize=20&pin=XTYXRGTpqcAKPURPsbAQzE7oeVP9kq2pYSH90mYt4m3fwcJlClpxrfmVYaGKuquQkdK3rLBQpEQH9V4tdrrh0w%3D%3D&name=%E8%B4%AD%E7%89%A9%E8%BD%A6"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,de;q=0.7,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Origin': 'https://lzkjdz-isv.isvjd.com',
        'Pragma': 'no-cache',
        'Referer': 'https://lzkjdz-isv.isvjd.com/wxAssemblePage/activity/67dfd244aacb438893a73a03785a48c7?activityId=67dfd244aacb438893a73a03785a48c7&adsource=tg_qrCode',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }
    try:
        response = requests.post(url=url_gwc, headers=headers, data=payload)
        result = response.json()
        lists = result['data']['homeInfoResultVOList']

        for _list in lists:
            activityId, shopName, activityUrl, updateTime = _list['activityId'], _list['shopName'], _list[
                'activityUrl'], _list['updateTime'],
            updateTime = ts2time(updateTime)
            print(activityId, shopName, activityUrl, updateTime)
            aa = (activityId, shopName, activityUrl, updateTime)
            data = f"{activityId}   {updateTime}   https://lzkjdz-isv.isvjd.com/wxCartKoi/cartkoi/activity?activityId={activityId}\n"
            cur_path = os.getcwd()
            try:
                with open('activity.txt', "a+", encoding="utf-8") as f:
                    f.write(data)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def task_hudong(cookie):
    # 粉丝互动
    url = "https://lzkjdz-isv.isvjd.com/wxAssemblePage/queryActInfo"

    payload = "pageNo=1&pageSize=20&pin=XTYXRGTpqcAKPURPsbAQzE7oeVP9kq2pYSH90mYt4m3fwcJlClpxrfmVYaGKuquQkdK3rLBQpEQH9V4tdrrh0w%3D%3D&name=%E4%BA%92%E5%8A%A8"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,de;q=0.7,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Origin': 'https://lzkjdz-isv.isvjd.com',
        'Pragma': 'no-cache',
        'Referer': 'https://lzkjdz-isv.isvjd.com/wxAssemblePage/activity/67dfd244aacb438893a73a03785a48c7?activityId=67dfd244aacb438893a73a03785a48c7&adsource=tg_qrCode',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }
    try:
        response = requests.post(url=url, headers=headers, data=payload)
        result = response.json()
        lists = result['data']['homeInfoResultVOList']

        for _list in lists:
            activityId, shopName, activityUrl, updateTime = _list['activityId'], _list['shopName'], _list[
                'activityUrl'], _list['updateTime'],
            updateTime = ts2time(updateTime)
            print(activityId, shopName, activityUrl, updateTime)
            data = f"{activityId}   {updateTime}   https://lzkjdz-isv.isvjd.com/wxCartKoi/cartkoi/activity?activityId={activityId}\n"
            try:
                with open('hudong.txt', "a+", encoding="utf-8") as f:
                    f.write(data)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


mac_env("jdwxck")
ql_env("jdwxck")

if __name__ == "__main__":
    global ckArr
    for inx, data in enumerate(ckArr):
        ck = data.split("&")
        print(ck[0])
        # task_gwc(ck[0])
        task_hudong(ck[0])
