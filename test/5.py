#!/usr/bin/python
# -*- coding: utf-8 -*-
import binascii

from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


# secret_str = des_encrypt('testtest', 'abc')
# print('密文:', secret_str)
# clear_str = des_decrypt('testtest', secret_str)
# print('明文:', clear_str)

secret_str = des_encrypt('abcdabcd', 'abc')
print('密文:', secret_str)
print(secret_str)
