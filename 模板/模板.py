# !/bin/env python3
# -*- coding: utf-8 -*

account = 1
printT = ''
ckArr = ''

# =================================以下代码不懂不要随便乱动=================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    import datetime
    import random
except Exception as e:
    print(e)

# requests.packages.urllib3.disable_warnings()  # 移除ssl证书错误警告


def printT(s):
    print("[【{0}】]: {1}".format(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s))
    sys.stdout.flush()


def Mac_env():
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    # print(path)
    with open(path, "r+") as f:
        env = f.read()
        if "tpyqc_data" in env:
            r = re.compile(r'tpyqc_data="(.*?)"', re.M | re.S | re.I)
            ckArr = []
            data = r.findall(env)
            print(data)
            if '@' in data[0]:
                ck = data[0].split('@')
                ckArr = ck
            elif '\n' in data[0]:
                ck = data[0].split('\n')
                ckArr = ck
            else:
                ckArr = data[0]
                print(ckArr)
        else:
            print("检查变量 tpyqc_data 是否已填写")


def ql_env():
    global ckArr
    if "tpyqc_data" in os.environ:
        ckArr = []
        # print(os.environ["tpyqc_data"])
        data = os.environ["tpyqc_data"]
        if '@' in data:
            ck = data.split('@')
            ckArr = ck
        elif '\n' in data:
            ck = data.split('\n')
            ckArr = ck
            print(ckArr)
        else:
            ckArr = data


Mac_env()

print(ckArr[0])
print(ckArr[1])
# 执行登录


def login(tpyqc_data, account):
    try:
        url = 'https://mrobot.pcauto.com.cn/auto_passport3_back_intf/passport3/rest/login_new.jsp'
        data = 'password={ck[1]}&username={ck[0]}'
        hearders = {
            # "user-agent": f"SFMainland_Store_Pro/9.37.1 (iPhone; iOS 15.0; Scale/2.00)",
            # "cookie": f"{tpyqc_data}",
            # "Accept-Encoding": "gzip, deflate, br",
            # "accept-language": "zh-CN,zh-Hans;q=0.9",
            # "accept": "application/json, text/plain, */*",
            # "Host": "mcs-mimp-web.sf-express.com",
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = requests.post(
            url=url, headers=hearders, data=data, verify=False)
        result = response.json()
        print(result)
        hasFinishSign = result['obj']['hasFinishSign']
        if hasFinishSign == 1:
            msg("【账号{0}】今日已签到 ,无需重复签到".format(account))
        else:
            countDay = result['obj']['countDay']
            commodityName = result['obj']['integralTaskSignPackageVOList'][0]['commodityName']
            msg("【账号{0}】今日签到成功 ,连续签到{1}天 ,获得【{2}】".format(
                account, countDay, commodityName))

    except Exception as e:
        print(e)
        msg("【账号{}】签到失败 ,可能是Cookie过期".format(account))


# # 做任务 get
# def do_mission(tpyqc_data, title, taskCode, account):
#     url = f'https://mcs-mimp-web.sf-express.com/mcs-mimp/task/finishTask?id={taskCode}'
#     hearders = {
#         "user-agent": f"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 mediaCode=SFEXPRESSAPP-iOS-ML",
#         "Cookie": f"{tpyqc_data}",
#         "Accept-Encoding": "gzip, deflate, br",
#         "accept-language": "zh-CN,zh-Hans;q=0.9",
#         "accept": "*/*",
#         "Host": "mcs-mimp-web.sf-express.com",
#     }
#     response = requests.get(url=url, headers=hearders, verify=False)
#     result = response.json()
#     print(result)
#     success = result['success']
#     if success == True:
#         printT("【账号{0}】正在执行【{1}】任务 ,等待20秒".format(account, title))
#         time.sleep(20)


# 获取通知服务
class msg(object):
    def __init__(self, m=''):
        self.str_msg = m
        self.message()

    def message(self):
        global msg_info
        printT(self.str_msg)
        try:
            msg_info = "{}\n{}".format(msg_info, self.str_msg)
        except:
            msg_info = "{}".format(self.str_msg)
        sys.stdout.flush()  # 这代码的作用就是刷新缓冲区。
        # 当我们打印一些字符时 ,并不是调用print函数后就立即打印的。一般会先将字符送到缓冲区 ,然后再打印。
        # 这就存在一个问题 ,如果你想等时间间隔的打印一些字符 ,但由于缓冲区没满 ,不会打印。就需要采取一些手段。如每次打印后强行刷新缓冲区。

    def getsendNotify(self, a=0):
        if a == 0:
            a += 1
        try:
            url = 'https://gitee.com/curtinlv/Public/raw/master/sendNotify.py'
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

    def main(self):
        global send
        cur_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.append(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            try:
                from sendNotify import send
            except:
                self.getsendNotify()
                try:
                    from sendNotify import send
                except:
                    printT("加载通知服务失败~")
        else:
            self.getsendNotify()
            try:
                from sendNotify import send
            except:
                printT("加载通知服务失败~")

        ###################
msg().main()
nowtime = int(round(time.time() * 1000))


if __name__ == '__main__':
    global msg_info
    print("============脚本只支持青龙新版=============\n")
    print("具体教程以文本模式打开文件 ,查看顶部教程\n\n")
    print("============执行太平洋汽车APP签到脚本==============")
    a = 1
    if cookies != '':
        for tpyqc_data in cookies:
            if a <= account:
                msg("★★★★★正在执行【账号{}】的任务★★★★★".format(a))
                # login(tpyqc_data, a)
                print("登录")
            else:
                break
    elif tpyqc_data != '':
        # login(tpyqc_data, a)
        print("登录")
    if '成功' in msg_info:
        send("太平洋汽车", msg_info)
    if '过期' in msg_info:
        send("太平洋汽车", msg_info)
