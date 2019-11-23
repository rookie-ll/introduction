from wxpy import *  # 导入模块

bot = Bot(cache_path=True)  # 扫码登陆
tuling = Tuling(api_key='726d317beed04382a81f7e42b53ec825')  # 初始化图灵机器人


@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


# 自动回复功能，回复所有消息
bot.join()  # 开始运行

