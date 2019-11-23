#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-17 11:18:05
# @Author  : wangjian
# @Link    : https://example.org
# @Version : $Id$
from Crypto.Cipher import DES
from binascii import b2a_hex, a2b_hex
class MyDESCrypt: #自己实现的DES加密类
    def __init__(self, key = ''):
        #密钥长度必须为64位，也就是8个字节
        if key is not '':
            self.key = key.encode('utf-8')
        else:
            self.key = '12345678'.encode('utf-8')
        self.mode = DES.MODE_CBC
    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self,text):
        try:
            text = text.encode('utf-8')
            cryptor = DES.new(self.key, self.mode, self.key)
            # 这里密钥key 长度必须为16（DES-128）,
            # 24（DES-192）,或者32 （DES-256）Bytes 长度
            # 目前DES-128 足够目前使用
            length = 16   #lenth可以设置为8的倍数
            count = len(text)
            if count < length:
                add = (length - count)
                # \0 backspace
                # text = text + ('\0' * add)
                text = text + ('\0' * add).encode('utf-8')
            elif count > length:
                add = (length - (count % length))
                # text = text + ('\0' * add)
                text = text + ('\0' * add).encode('utf-8')
            self.ciphertext = cryptor.encrypt(text)
            # 因为DES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
            # 所以这里统一把加密后的字符串转化为16进制字符串
            return b2a_hex(self.ciphertext)
        except:
            return ""
    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        try:
            cryptor = DES.new(self.key, self.mode, self.key)
            plain_text = cryptor.decrypt(a2b_hex(text))
            # return plain_text.rstrip('\0')
            return bytes.decode(plain_text).rstrip('\0')
        except:
            return ""