# !/bin/env python3
# -*- coding: utf-8 -*
from cmath import e
import datetime
import time
import sys
import json
import re
import os

ckArr = []


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


Mac_env(1, 2)
ql_env(1, 2)

print(ckArr)
