# !/bin/env python3
# -*- coding: utf-8 -*
"""
    new Env("预言")
    Name: 预言  网页     虚拟币,自己零撸  被坑了钱别找我
    Author: yml
    Date: 2022.8.17
    cron: 19 7,12 * * *    prophecy.py

    7.12    增加通知
    ================== 青龙--配置文件 ==================
    变量格式: export prophecy_data=" rem_token @ rem_token "    多账号用 换行 或 @ 分割

    教程:  需要自行用手机抓取 wprophecy.com  域名的包 , 抓 rem_token
"""
# ================================= 以下代码不懂不要随便乱动 ====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    import random
except Exception as e:
    print(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "预言"
Name_Pinyin = "prophecy"
Script_Change = "每日签到, 每天预言无战争 100投入"
Script_Version = "0.1.1"


# --------------------------------------------------------------------------------------------


class Script:
    def __init__(self, rem_token):
        self.rem_token = rem_token
        # self.PHPSESSID = phpsessid

    # noinspection PyMethodMayBeStatic
    def url(self, name):  # hostname + xxxx
        url = f"https://wprophecy.com/{name}"
        return url

    def headers(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'cookie': f"REM_TOKEN={self.rem_token}",
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
        }
        # print(headers)
        return headers

    def csrf_token(self, name="更新 csrf-token"):  # 获取 csrf-token
        try:
            response = requests.get(url=self.url("getCSRFToken"), headers=self.headers(), verify=False)
            result = response.json()

            if result['status'] == 1:
                msg(f"{name}: 成功!")
                # print(result['data']['CSRF-TOKEN'])
                return result['data']['CSRF-TOKEN']
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def headers2(self):
        headers2 = {
            'accept': 'application/json, text/plain, */*',
            'cookie': self.rem_token,
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'csrf-token': self.csrf_token()
        }
        # print(headers)
        return headers2

    def do_sign(self, name):  # 执行签到奖励
        try:
            payload = {}
            response = requests.post(url=self.url("user/login/reward/claim"), headers=self.headers2(), data=payload,
                                     verify=False)
            result = response.json()

            if result['status'] == 1:
                msg(f"{name}: 成功, 获得100礼金!")
                time.sleep(3)
            elif result['status'] == 0:
                msg(f"{name}: {result['error']}, 已申请过奖励!")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def user_info(self, name="用户信息"):  # 用户信息
        try:
            response = requests.get(url=self.url("user/appuser/info"), headers=self.headers())
            result = response.json()
            # print(result)
            if result['status'] == 1:
                phone = result['data']['data']['contactNo']
                msg(f"{name}: 成功!\n欢迎:{phone[:3]}****{phone[-4:]}, 余额: {float(result['data']['data']['wallet']['balance'])} USDT, 邀请码: {result['data']['data']['referralCode']}")
                time.sleep(3)
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)

    def prophecy_list(self, name="预言列表"):  # 预言列表
        try:
            response = requests.get(url=self.url("betting/hottest/result/zh-hans"), headers=self.headers())
            result = response.json()
            # print(result)
            if result['status'] == 1:
                msg(f"共找到{result['data']['itemsCount']}个活动预言, 随机选择一个进行预言")

                print(type(result['data']['itemsCount']))
                items = result['data']['items']
                # num = random(result['data']['items'])
                print(random.randint(0, result['data']['items']))
                # print(items)
                for item in items:
                    if item['roundTemplateId'] == "29":
                        print(item['roundId'])

                time.sleep(3)
            elif result['status'] == 0:
                msg(f"{name}: 失败, 请检查变量&脚本更新到最新再试试")
                print('美国 vs 中国111')
            else:
                msg(f"{name}: 失败, 请稍后再试!")
                print(result)
        except Exception as err:
            print(err)


# ====================================================================


def main():
    pass


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
            r = re.compile(r'prophecy_data="(.*?)"', re.M | re.S | re.I)
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


# 通知服务
class Msg(object):
    def __init__(self, m=''):
        self.str_msg = m
        self.message()

    # noinspection PyMethodMayBeStatic
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


def msg(data):
    Msg(data)


mac_env(f"{Name_Pinyin}_data")
ql_env(f"{Name_Pinyin}_data")


def tip():
    print("================ 脚本只支持青龙面板 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    msg(f"🔔 {Script_Name} ,开始! ")
    origin_version = last_version(Name_Pinyin, 1)
    msg(f"📌 本地脚本: {Script_Version}      远程仓库版本: V {origin_version}")
    msg(f"📌 🆙 更新内容: {Script_Change}")
    msg(f"共发现 {str(len(ckArr))} 个账号")


def start():
    for inx, data in enumerate(ckArr):
        msg("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        # print(ck[0])
        # print(ck[1])
        prophecy = Script(ck[0])
        # prophecy.do_sign("签到")
        # prophecy.user_info("用户信息")
        prophecy.prophecy_list("预言列表")

        # prophecy.sign_info("签到信息")
        # prophecy.get_rice("偷大米")
        # prophecy.get_index_info("获取可收取大米信息")
        # prophecy.cookie()


if __name__ == "__main__":
    global ckArr, msg_info, send
    tip()
    start()
    send(f"{Script_Name}", msg_info)
