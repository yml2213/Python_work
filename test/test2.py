import os
import re
import sys
import time
from urllib.parse import quote

import requests


# 通知服务
class Msg(object):
    def __init__(self, m=''):
        self.str_msg = m
        self.message()

    def get_sendnotify(self):
        if not os.path.exists("sendNotify.py"):
            cur_path = os.getcwd()
            print(f"未找到通知依赖文件,将于脚本执行目录({cur_path})新建:sendNotify.py ")
            try:
                url = 'https://raw.gh.fakev.cn/yml2213/Python/master/sendNotify.py'
                response = requests.get(url)
                with open('sendNotify.py', "w+", encoding="utf-8") as f:
                    f.write(response.text)
            except Exception as err:
                print(err)
        else:
            print("文件已存在,跳过")
            pass

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            # msg_info = ''
            msg_info = f"{msg_info}\n{self.str_msg}"
        except Exception as err:
            print(err)
            msg_info = "{}".format(self.str_msg)
        sys.stdout.flush()
        # 这代码的作用就是刷新缓冲区。
        # 当我们打印一些字符时 ,并不是调用print函数后就立即打印的。一般会先将字符送到缓冲区 ,然后再打印。
        # 这就存在一个问题 ,如果你想等时间间隔的打印一些字符 ,但由于缓冲区没满 ,不会打印。就需要采取一些手段。如每次打印后强行刷新缓冲区。

    def main(self):
        global send
        cur_path = os.getcwd()
        # print(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            # noinspection PyBroadException
            try:
                from sendNotify import send
            except Exception as err:
                self.get_sendnotify()
                print(err)
                try:
                    from sendNotify import send
                except Exception as err:
                    print(err)
                    print("加载通知服务失败~")
        else:
            self.get_sendnotify()
            try:
                from sendNotify import send
            except Exception as err:
                print(err)
                print("加载通知服务失败~")


Msg().main()


def mac_env(name):
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    with open(path, "r+") as f:
        env = f.read()
        if name in env:
            r = re.compile(r'jdwxck="(.*?)"', re.M | re.S | re.I)
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


def task(name, cookie):
    # 购物车
    url = "https://lzkjdz-isv.isvjd.com/wxAssemblePage/queryActInfo"
    print(name)
    wd = quote(name)
    print(wd)
    print(url)
    payload = f"pageNo=1&pageSize=20&pin=XTYXRGTpqcAKPURPsbAQzE7oeVP9kq2pYSH90mYt4m3fwcJlClpxrfmVYaGKuquQkdK3rLBQpEQH9V4tdrrh0w%3D%3D&name={wd}"
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
            activityId, activityUrl, updateTime = _list['activityId'], _list['activityUrl'], _list['updateTime'],
            updateTime = ts2time(updateTime)
            print(activityId, activityUrl, updateTime)
            data = f"{activityId}   {updateTime}   {activityUrl}\n"
            Msg(data)
            f_name = f"{name}.txt"
            try:
                with open(f_name, "a+", encoding="utf-8") as f:
                    f.write(data)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


mac_env("jdwxck")
ql_env("jdwxck")
if __name__ == "__main__":
    global ckArr, msg_info, send
    for inx, data in enumerate(ckArr):
        ck = data.split("&")
        # print(ck[0])
        # print(ck[1])
        task(ck[0], ck[1])
        send(f"京东无线   {ck[0]}", msg_info)
