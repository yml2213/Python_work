# !/bin/env python3
# -*- coding: utf-8 -*
"""
    new Env("观海新闻")
    Name: 观海新闻  邀请码 bx0337   感谢填写,你的支持就是我的动力
    Author: yml
    Date: 2022.7.8
    cron: 19 7 * * *    ghxw.py


    感谢 一峰一燕 提供技术支持
    ================== 青龙--配置文件 ==================
    变量格式: export ghxw_data=" memberid @ memberid "   ,多账号用 换行 或 @ 分割

    教程:  需要自行用手机抓取 m-api.guanhai.com.cn 域名的包 , memberid 是 headers 中的参数
"""
# ================================= 以下代码不懂不要随便乱动 ====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
except Exception as e:
    print(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "观海新闻"
Name_Pinyin = "ghxw"
Script_Change = "观海新闻  基本完成所有任务"
Script_Version = "0.0.1"


# --------------------------------------------------------------------------------------------

def last_version(name, mold):
    url = ''
    if mold == 1:
        url = f"https://raw.gh.fakev.cn/yml2213/Python/master/{name}/{name}.py"

    elif mold == 2:
        url = f"http://yml-gitea.ml:2233/yml/Python/raw/branch/master/{name}.py"
    try:
        _url = url
        _headers = {}
        response = requests.get(url=_url, headers=_headers, verify=False)
        result = response.text
        r = re.compile(r'Script_Version = "(.*?)"')
        _data = r.findall(result)
        if not _data:
            return "出现未知错误 ,请稍后重试!"
        else:
            return _data[0]
    except Exception as err:
        print(err)


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


def md5_encrypt(_data):
    import hashlib
    md5 = hashlib.md5()
    md5.update(_data.encode(encoding='utf-8'))
    return md5.hexdigest()


def get_sign(memberid, name, device_id):
    salt = "9544309039a91e9d8ae0bd07f3ca90ef"
    t = time.time()
    ts = int(round(t * 1000))
    ts_ = ts - 2
    # print("ts: ", ts)
    # print("ts_: ", ts_)
    ts = str(ts)

    _data = f'app_version=1.7.2&clientid=1&contentId={memberid}_{ts_}&creditType={name}&device_id={device_id}&ip=10.0.0.26&memberId={memberid}&memberid={memberid}&modules=common%3A1&siteid=10001&system_name=android&type=android'
    # print(_data)
    md5_encrypt(_data)
    # print(md5_encrypt(_data))
    sign = md5_encrypt(md5_encrypt(_data) + salt + ts)
    # print(md5_encrypt(data) + salt + ts)
    # print(sign)
    return sign, ts, ts_, device_id


def get_device_id():
    import random
    import string
    random_12 = ''.join(random.sample(string.digits + string.ascii_lowercase, 12))
    _id = f"0f1be1ff-44b7-47cb-afca-{random_12}"
    return _id


def get_params(memberid, name, sign, ts, ts_, device_id):
    params = {
        'clientid': '1',
        'device_id': device_id,
        'app_version': '1.7.2',
        'ip': '10.0.0.26',
        'system_name': 'android',
        'contentId': f'{memberid}_{ts_}',
        'sign': sign,
        'type': 'android',
        'modules': 'common:1',
        'creditType': name,
        'siteid': '10001',
        'time': ts,
        'memberid': memberid,
        'memberId': memberid
    }
    return params


def get_sign2(memberid, device_id):
    salt = "9544309039a91e9d8ae0bd07f3ca90ef"
    t = time.time()
    ts = int(round(t * 1000))
    # print("ts: ", ts)
    ts = str(ts)
    _data = f"app_version=1.7.2&clientid=1&device_id={device_id}&ip=10.0.0.26&memberid={memberid}&modules=task%3A1&siteid=10001&system_name=android&type=android"
    # print(_data)
    md5_encrypt(_data)
    # print(md5_encrypt(_data))
    sign = md5_encrypt(md5_encrypt(_data) + salt + ts)
    # print(md5_encrypt(data) + salt + ts)
    # print(sign)
    return sign, ts, device_id


def get_params2(memberid, sign, ts, device_id):
    params = {
        'clientid': '1',
        'device_id': device_id,
        'app_version': '1.7.2',
        'ip': '10.0.0.26',
        'system_name': 'android',
        'sign': sign,
        'siteid': '10001',
        'time': ts,
        'type': 'android',
        'modules': 'task:1',
        'memberid': memberid
    }
    return params, device_id


class Script:
    def __init__(self, memberid):
        self.memberid = memberid

    url = "https://m-api.guanhai.com.cn/v2/creditnew"
    headers = {
        'Host': 'm-api.guanhai.com.cn',
        'User-Agent': 'okhttp/3.11.0'
    }

    def task_list(self):
        device_id = get_device_id()
        s = get_sign2(self.memberid, device_id)
        sign, ts, device_id = s[0], s[1], s[2]
        p = get_params2(self.memberid, sign, ts, device_id)
        params, device_id = p[0], p[1]

        print("开始 任务列表")
        try:
            response = requests.get(url=self.url, params=params, headers=self.headers, verify=False)
            # print(response.url)
            result = response.json()
            # print(result)
            if result["state"]:
                task_arr = result['data']['task']['list']
                if len(task_arr) == 2:
                    print("新手任务请自行完成")
                    task_arr = result['data']['task']['list'][1]['list']
                elif len(task_arr) == 1:
                    task_arr = result['data']['task']['list'][0]['list']

                for task in task_arr:
                    _max = int(task['max_times'])
                    _completed = int(task['completed_times'])
                    print(task['name'], ":", _completed, "/", _max)
                    self.task_plan(task['name'], _max - _completed, device_id)
            elif not result["state"]:
                pass
            else:
                print(f"{'name'}: 失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)

    def do_task(self, name, device_id):
        r = get_sign(self.memberid, name, device_id)
        sign, ts, ts_, device_id = r[0], r[1], r[2], r[3]
        p = get_params(self.memberid, name, sign, ts, ts_, device_id)
        # print(f"开始 {name}任务")
        # time.sleep(2)
        try:
            response = requests.get(url=self.url, params=p, headers=self.headers, verify=False)
            result = response.json()
            # print(result)
            if result["state"]:
                print(f"{name}: {result['message']}")
                time.sleep(5)
                return
            elif not result["state"]:
                print(f"{name}: {result['error']}")
            else:
                print(f"{name}: 失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)

    def task_plan(self, name, num, device_id):
        try:
            if name == "启动":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_LOGIN", device_id)
            elif name == "阅读":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_READ", device_id)
            elif name == "评论":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_COMMENT", device_id)
            elif name == "分享":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_SHARE", device_id)
            elif name == "点赞":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_LIKE", device_id)
            elif name == "收藏":
                for i in range(num):
                    print(f"第 {i + 1} 次 {name}")
                    self.do_task("SYS_COLLECT", device_id)
            elif name == "邀请":
                pass
        except Exception as err:
            print(err)


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
        pass

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            msg_info = ''
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

mac_env(f"{Name_Pinyin}_data")
ql_env(f"{Name_Pinyin}_data")


def tip():
    print("================ 脚本只支持青龙新版 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    print(f"🔔 {Script_Name} ,开始! ")
    origin_version = last_version(Name_Pinyin, 2)
    print(f"📌 本地脚本: {Script_Version}      远程仓库版本: V {origin_version}")
    print(f"📌 🆙 更新内容: {Script_Change}")
    print(f"共发现 {str(len(ckArr))} 个账号")


def start():
    for inx, data in enumerate(ckArr):
        print("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        ghxw = Script(ck[0])
        ghxw.task_list()


if __name__ == "__main__":
    global ckArr, msg_info, send
    tip()
    start()
    send(f"{Name_Pinyin}", msg_info)
