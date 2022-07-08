# !/bin/env python3
# -*- coding: utf-8 -*

import os


ckArr = ''


def ql_env(ck, Variables):
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


ql_env(1, 2)
print(ckArr)
