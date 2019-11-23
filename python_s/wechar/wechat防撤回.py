#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'jiangwenwen'

import itchat
from itchat.content import *
import time
import re
import os

print("该程序由里客云资源站开发，网址：likeyunba.com")
print("作者:TANKING")
print("打开程序会弹出一个二维码，微信扫码")
print("如果二维码弹不出，那就在你这个程序的同一个目录下找到QR.png双击打开扫码")
print("扫码后，出现Start auto replying就可以实时监控消息了...")

msg_information = {}
# 针对表情包的内容
face_bug = None

@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isMpChat=True)
def handle_receive_msg(msg):
    global face_bug
    # 接收消息的时间
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 在好友列表列表中查询发送信息的好友昵称
    msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # 信息发送的时间
    msg_time = msg['CreateTime']
    # 每条信息的ID
    msg_id = msg['MsgId']
    # 储存信息的内容
    msg_content = None
    # 储存分享的连接，比如分享的文章和音乐
    msg_share_url = None

    # 如果发送的消息是文本或者好友推荐
    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
        msg_content = msg['Text']
        print(msg_content)

    # 如果发送的消息是附件，视频，图片，语音
    elif msg['Type'] == 'Attachment' or msg['Type'] == 'Video' \
        or msg['Type'] == 'Picture'\
            or msg['Type'] == 'Recording':
        # 内容为下载文件名
        msg_content = msg['FileName']
        msg['Text'](str(msg_content))

    # 如果消息是推荐的名片
    elif msg['Type'] == 'Card':
        # 内容是推荐人的昵称和性别
        msg_content = msg['RecommendInfo']['NickName'] + '的名片'
        if msg['RecommendInfo']['Sex'] == 1:
            msg_content += '性别为男'
        else:
            msg_content += '性别为女'

        print(msg_content)

    # 如果消息为分享的位置信息
    elif msg['Type'] == 'Map':
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            # 内容为详细地址
            msg_content = r'纬度->' + x.__str__() + "经度->" + y.__str__()
        else:
            msg_content = r"" + location

    # 如果消息是分享的音乐或者文章，详细的内容为文章的标题或者分享的名字
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_share_url = msg['Url']
        print(msg_share_url)
    face_bug = msg_content

    # 将信息存储在字典中，每一个msg_id对应一条消息
    msg_information.update(
        {
            msg_id: {
                "msg_from": msg_from, "msg_time": msg_time, "msg_time_rec": msg_time_rec,
                "msg_type": msg['Type'],
                "msg_content": msg_content, "msg_share_url": msg_share_url
            }
        }
)

#这个是用于监听是否有friend消息撤回
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def information(msg):
    # 这里如果这里的msg['Content']中包含消息撤回和id，就执行下面的语句
    if '撤回了一条消息' in msg['Content']:
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        # 得到消息
        old_msg = msg_information.get(old_msg_id)
        print(old_msg)

        # 如果发送的是表情
        if len(old_msg_id)<11:
            itchat.send_file(face_bug, toUserName='filehelper')
        # 发送撤回的提示给文件助手
        else:
            msg_body = "【"\
                       + old_msg.get('msg_from') + "撤回了】\n"\
                       + old_msg.get("msg_type") + "消息:" + "\n"\
                       + old_msg.get("msg_time_rec") + "\n"\
                       + r"" + old_msg.get("msg_content")

        # 如果分享的文件被撤回了，那么就将分享的url加在msg_body中发送给文件助手
        if old_msg['msg_type'] == "Sharing":
            msg_body += "\n就是这个链接>" + old_msg.get('msg_share_url')

        # 将撤回消息发送到文件助手
        itchat.send_msg(msg_body, toUserName="filehelper")

        # 有文件的话也要将文件发送回去
        if old_msg["msg_type"] == "Picture"\
                or old_msg["msg_type"] == "Recording"\
                or old_msg["msg_type"] == "Video"\
                or old_msg["msg_type"] == "Attachment":
            file = "@fil@%s" % (old_msg['msg_content'])
            itchat.send(msg=file, toUserName='filehelper')
            os.remove(old_msg['msg_content'])

        # 删除字典旧信息
        msg_information.pop(old_msg_id)

itchat.auto_login(hotReload=True)
itchat.run()