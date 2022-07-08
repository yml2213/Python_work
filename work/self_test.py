# !/bin/env python3
# -*- coding: utf-8 -*
# ================================= 以下代码不懂不要随便乱动 ====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    from loguru import logger
except Exception as e:
    logger.error(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "测试"
Name_Pinyin = "ceshi"
Script_Change = "Hello Python"
Script_Version = "0.0.1"
Version_Check = "0.0.2"

# --------------------------------------------------------------------------------------------
# Origin_Version=''
url = ''


def last_version(name, mold):
    global url
    if mold == 1:
        url = "https://raw.gh.fakev.cn/yml2213/Python/master/" + name + "/" + name + ".py"
    elif mold == 2:
        url = "http://yml-gitea.ml:2233/yml/JavaScript-yml/raw/branch/master/" + name + ".py"
    try:
        # print(url)
        info_url = url
        info_headers = {}
        response = requests.get(url=info_url, headers=info_headers, verify=False)
        result = response.text
        r = re.compile(r'Version_Check = "(.*?)"')
        data1 = r.findall(result)
        return data1[0]
    except Exception as err:
        print(err)


def tip():
    logger.info("================ 脚本只支持青龙新版 =================")
    logger.info("============ 具体教程以请自行查看顶部教程 =============\n")
    logger.info("🔔 " + Script_Name + " ,开始!")
    origin_version = last_version(Name_Pinyin, 1)
    print(origin_version)
    logger.info("📌 本地脚本: V " + Script_Version +
                "    远程仓库版本: V" + origin_version)
    logger.info("📌 🆙 更新内容: " + Script_Change)


def mac_env(tpyqc_data):
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    with open(path, "r+") as f:
        env = f.read()
        if tpyqc_data in env:
            r = re.compile(r'tpyqc_data="(.*?)"', re.M | re.S | re.I)
            result = r.findall(env)
            # print(data[0])
            if "@" in result[0]:
                ck = result[0].split("@")
                ckArr = ck
            elif "\n" in result[0]:
                ck = result[0].split("\n")
                ckArr = ck
            else:
                ckArr = result
        else:
            logger.warning("检查变量" + tpyqc_data + "是否已填写")


def ql_env(tpyqc_data):
    global ckArr
    if tpyqc_data in os.environ:
        ckArr = []
        data = os.environ[tpyqc_data]
        if "@" in data:
            ck = data.split("@")
            ckArr = ck
        elif "\n" in data:
            ck = data.split("\n")
            ckArr = ck
        else:
            ckArr = data


class Tpyqc:
    url_login = "https://mrobot.pcauto.com.cn/auto_passport3_back_intf/passport3/rest/login_new.jsp"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, phone, passwd):
        self.phone = phone
        self.passwd = passwd

    # data_login = "password=" + self.passwd + "&username=" + self.phone

    def login(self):
        try:
            _data = "password=" + self.passwd + "&username=" + self.phone
            response = requests.post(url=Tpyqc.url_login, headers=self.headers, data=_data, verify=False)
            result = response.json()
            print(result)

            if result["status"] == 0:
                # if result.status == 0:
                logger.info("登录: " + result["message"])
                # msg("登录: " + result["message"])
                session = result["session"]
                print(session)

            # else:
            #     countDay = result['obj']['countDay']
            #     commodityName = result['obj']['integralTaskSignPackageVOList'][0]['commodityName']
            #     msg("【账号{0}】今日签到成功 ,连续签到{1}天 ,获得【{2}】".format(
            #         account, countDay, commodityName))

        except Exception as err:
            print(err)
            # msg("【账号{}】签到失败 ,可能是Cookie过期".format(account))


mac_env("tpyqc_data")
ql_env("tpyqc_data")

if __name__ == "__main__":
    global msg_info
    global ckArr
    tip()

    for data in ckArr:
        ck = data.split("&")
        logger.info("开始 登录")
        print(ck)
        print(ck[0], ck[1])
        Tpyqc = Tpyqc(ck[0], ck[1])

        Tpyqc.login()
