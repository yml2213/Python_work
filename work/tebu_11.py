"""
const $ = new Env("特步签到");
东芝签到

cron:
0 7 * * * qd_dongzhi.py
"""

import requests

headers = {
    'Host': 'wxa-tp.ezrpro.com',
    'Connection': 'keep-alive',
    'Content-Length': '36',
    'ezr-cop-id': '143',
    'charset': 'utf-8',
    'ezr-vuid': '83088008',
    'uber-trace-id': '77d79268749913ba:77d79268749913ba:0:1',
    'ezr-sp': '2',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; 22041211AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2889 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/3644 MicroMessenger/8.0.15.2001(0x28000F41) Process/appbrand1 WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'ezr-source': 'weapp',
    'ezr-st': '1656633420785',
    'ezr-ss': '6cc54f20ca1f817eb7576fb19af5d370902940a7',
    'ezr-userid': 'oMfWKs_JZo7lhXJgTYpiTIpfyGsY',
    'ezr-sv': '1',
    'ezr-brand-id': '254',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx12e1cb3b09a0e6f0/70/page-frame.html'
}

data = '{"ActId":784,"ActRemindStatus":true}'


def sign():
    response = requests.post('https://wxa-tp.ezrpro.com/myvip/Vip/SignIn/SignIn', headers=headers, data=data)
    print(response.json())


if __name__ == '__main__':
    sign()
