# !/bin/env python3
# -*- coding: utf-8 -*
"""
    new Env("观海新闻")
    感谢 一峰一燕 提供脚本以及技术支持

    项目名称: 观海新闻
    Author: yml
    Date: 2022.7.8
    cron: 19 7 * * *    ghxw.py

    ================== 青龙--配置文件 ==================
    变量格式: export ghxw_data=" memberid @ memberid "   ,多账号用 换行 或 @ 分割

    【教程】:  需要自行用手机抓取 wxa-tp.ezrpro.com 域名的包 , memberid 是 headers 中的参数

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
Script_Change = "观海新闻商城签到 ,第一个 py 脚本"
Script_Version = "0.1.2"
Version_Check = "0.1.2"


# --------------------------------------------------------------------------------------------


def last_version(name, mold):
    url = ''
    if mold == 1:
        url = f"https://raw.gh.fakev.cn/yml2213/Python/master/{name}/{name}.py"

    elif mold == 2:
        url = f"http://yml-gitea.ml:2233/yml/JavaScript-yml/raw/branch/master/{name}.py"

    try:
        _url = url
        _headers = {}
        response = requests.get(url=_url, headers=_headers, verify=False)
        result = response.text
        r = re.compile(r'Version_Check = "(.*?)"')
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


def get_sign(memberid, name):
    salt = "9544309039a91e9d8ae0bd07f3ca90ef"
    t = time.time()
    ts = int(round(t * 1000))
    ts_ = ts - 2
    # print("ts: ", ts)
    # print("ts_: ", ts_)
    ts = str(ts)
    _data2 = f"app_version=1.7.2&clientid=1&device_id=0f1be1ff-44b7-47cb-afca-99a292820f03&ip=10.0.0.26&memberid=137505&modules=task%3A1&siteid=10001&system_name=android&type=android"

    _data = f'app_version=1.7.2&clientid=1&contentId={memberid}_{ts_}&creditType={name}&device_id=0f1be1ff-44b7-47cb-afca-99a292820f03&ip=10.0.0.26&memberId={memberid}&memberid={memberid}&modules=common%3A1&siteid=10001&system_name=android&type=android'
    # print(_data)
    md5_encrypt(_data)
    # print(md5_encrypt(_data))
    sign = md5_encrypt(md5_encrypt(_data) + salt + ts)
    # print(md5_encrypt(data) + salt + ts)
    # print(sign)
    return sign, ts, ts_


def get_params(memberid, name, sign, ts, ts_):
    params = {
        'clientid': '1',
        'device_id': '0f1be1ff-44b7-47cb-afca-99a292820f03',
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


def get_sign2(memberid):
    salt = "9544309039a91e9d8ae0bd07f3ca90ef"
    t = time.time()
    ts = int(round(t * 1000))
    # print("ts: ", ts)
    ts = str(ts)
    _data = f"app_version=1.7.2&clientid=1&device_id=0f1be1ff-44b7-47cb-afca-99a292820f03&ip=10.0.0.26&memberid={memberid}&modules=task%3A1&siteid=10001&system_name=android&type=android"
    # print(_data)
    md5_encrypt(_data)
    # print(md5_encrypt(_data))
    sign = md5_encrypt(md5_encrypt(_data) + salt + ts)
    # print(md5_encrypt(data) + salt + ts)
    # print(sign)
    return sign, ts


def get_params2(memberid, sign, ts):
    params = {
        'clientid': '1',
        'device_id': '0f1be1ff-44b7-47cb-afca-99a292820f03',
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
    return params


mac_env("ghxw_data")
ql_env("ghxw_data")


class Script:
    def __init__(self, memberid):
        self.memberid = memberid

    url = "https://m-api.guanhai.com.cn/v2/creditnew"
    headers = {
        'Host': 'm-api.guanhai.com.cn',
        'User-Agent': 'okhttp/3.11.0'
    }

    def task_list(self):
        r = get_sign2(self.memberid)
        (sign, ts) = (r[0], r[1])
        p = get_params2(self.memberid, sign, ts)
        print("开始 任务列表")
        try:
            response = requests.get(url=self.url, params=p, headers=self.headers, verify=False)
            print(response.url)
            result = response.json()
            # print(result)
            if result["state"]:
                task_arr = result['data']['task']['list']
                if len(task_arr) == 2:
                    print("新手任务请自行完成")
                    task_arr = result['data']['task']['list'][1]['list']
                elif len(task_arr) == 1:
                    task_arr = result['data']['task']['list'][0]['list']

                print(task_arr)
                print('=============')

                # for task in task_arr:
                #     print(task)

                print(f": {result['message']}")
                return
            elif not result["state"]:
                pass
            else:
                print(f"{'name'}: 失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)

    def task(self, name):
        r = get_sign(self.memberid, name)
        (sign, ts, ts_) = (r[0], r[1], r[2])
        p = get_params(self.memberid, name, sign, ts, ts_)
        print("开始 任务")
        try:
            response = requests.get(url=self.url, params=p, headers=self.headers, verify=False)
            result = response.json()
            # print(result)
            if result["state"]:
                print(f"{name}: {result['message']}")
                return
            elif not result["state"]:
                print(f"{name}: {result['error']}")
            else:
                print(f"{name}: 失败 ,请检查 变量 是否正确!")
        except Exception as err:
            print(err)


def tip():
    global ckArr
    print("================ 脚本只支持青龙新版 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    print(f"🔔 {Script_Name} ,开始! ")
    origin_version = last_version(Name_Pinyin, 1)
    print(f"📌 本地脚本: {Script_Version}      远程仓库版本: V {origin_version}")
    print(f"📌 🆙 更新内容: {Script_Change}")
    print(f"共发现 {str(len(ckArr))} 个账号")


if __name__ == "__main__":
    global ckArr
    tip()
    for inx, data in enumerate(ckArr):
        print("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        ghxw = Script(ck[0])
        # print(ck)
        ghxw.task_list()

        # ghxw.task("SYS_LOGIN")
        # ghxw.task("SYS_READ")
        # ghxw.task("SYS_SHARE")
        # ghxw.task("SYS_COMMENT")
        # ghxw.task("SYS_LIKE")
        # ghxw.task("SYS_COLLECT")
