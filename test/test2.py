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


class Script:
    def __init__(self, memberid):
        self.memberid = memberid

    def task_list(self):
        print("开始 任务列表")

        # msg("你好11")
        # msg("你好22")

        Msg(f"nihei,你好11")
        Msg(f"nihei,你好22")
        send("我是一个标题", msg_info)

        # send("我是一个标题",content) #名字


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

# mac_env(f"{Name_Pinyin}_data")
ql_env(f"{Name_Pinyin}_data")


def tip():
    print("================ 脚本只支持青龙新版 =================")
    print("============ 具体教程以请自行查看顶部教程 =============\n")
    print(f"🔔 {Script_Name} ,开始! ")
    origin_version = last_version(Name_Pinyin, 2)
    print(f"📌 本地脚本: {Script_Version}      远程仓库版本: V {origin_version}")
    print(f"📌 🆙 更新内容: {Script_Change}")
    print(f"共发现 {str(len(ckArr))} 个账号")


if __name__ == "__main__":

    global ckArr, msg_info, send, msg_lj
    tip()
    for inx, data in enumerate(ckArr):
        print("=============== 开始第" + str(inx + 1) + "个账号 ===============")
        ck = data.split("&")
        ghxw = Script(ck[0])
        ghxw.task_list()

    send(f"{Name_Pinyin}", msg_info)
