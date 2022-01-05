import json
import requests
import random
import time
from discord_webhook import DiscordWebhook#pip install discord_webhook

#v2rayN本地代理
#因为需要访问外网
proxy = {'http': 'http://127.0.0.1:10809',
         'https': 'http://127.0.0.1:10809',
         'http': 'socks5://127.0.0.1:10808',
         'https': 'socks5://127.0.0.1:10808'}


#配置信息 替换""内信息
token="###"
serverid = "###"#服务器ID
channelid = "###"#频道ID


#语言库 可自行添加
mss = '''
{
  "bot": [
    {
      "message": "所以我先肝为敬"
    },
    {
      "message": "肝起来"
    },
    {
      "message": "升一等大概花多久啊兄弟們"
    },
    {
      "message": "好想升級啊"
    },
    {
      "message": "太屌了！"
    },
    {
      "message": "冲鸭"
    },
    {
      "message": "纯粹的冲"
    },
    {
      "message": "升一等大概沖多久"
    },
    {
      "message": "冲吧，我都要快疯了。"
    },
    {
      "message": "真的牛逼"
    },
    {
      "message": "我疯了"
    },
    {
      "message": "白名单我来了"
    },
    {
      "message": "争取天亮前肝到"
    },
    {
      "message": "加油，不要放弃"
    },
    {
      "message": "肝呀"
    },
    {
      "message": "我们可以的"
    },
    {
      "message": "你狠厲害呀"
    },
    {
      "message": "今天肝 "
    },
    {
      "message": "哈哈哈哈"
    },
    {
      "message": "加油啊"
    },
    {
      "message": "还有多久啊"
    },
    {
      "message": "加油兄弟们"
    },
    {
      "message": "不知道给几天时间？"
    },
    {
      "message": "起飞"
    },
    {
      "message": "肝爆"
    },
    {
      "message": "感谢"
    },
    {
      "message": "给我升升升"
    },
    {
      "message": "你们多少级了"
    },
    {
      "message": "拿白规则只会越来越严"
    },
    {
      "message": "肝吧"
    },
    {
      "message": "哈哈哈哈"
    },
    {
      "message": "吃饭"
    },
    {
      "message": "牛牛牛"
    },
    {
      "message": "哎"
    },
    {
      "message": "肝爆他"
    },
    {
      "message": "那就早点放弃"
    },
    {
      "message": "看起来像机器+人工"
    },
    {
      "message": "兄弟们，我觉得我们都有希望的"
    },
    {
      "message": "水了大半天了"
    },
    {
      "message": "都要肝肾亏了"
    },
    {
      "message": "赶紧升级"
    },
    {
      "message": "我完全純手工"
    },
    {
      "message": "你还差多少啊"
    },
    {
      "message": "小心啥啊 各位哦"
    },
    {
      "message": "加油吧大家"
    },
    {
      "message": "竞争太大了"
    },
    {
      "message": "冲到明天"
    },
    {
      "message": "升级为王"
    },
    {
      "message": "哈哈"
    },
    {
      "message": "各位加油～"
    },
    {
      "message": "哈哈哈"
    }
  ]
}
'''  
header_data = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "authorization": token,
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/"+serverid+"/"+channelid+""
}
url="https://discord.com/api/v9/channels/"+channelid+"/messages"
myfriend = json.loads(mss)
def abc():
    a = ""
    while True:
        try:
          print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
          mssage = myfriend["bot"][random.randint(0,len(myfriend["bot"])-1)]["message"]#随机话术
          if a != mssage:
              mss_data = {"content": mssage,
                          "tts": "false",}
              r=requests.post(url=url,headers=header_data,data=mss_data,proxies=proxy)#如果不使用本地代理请删除 ,proxies=proxy
              if 199 < r.status_code < 300:
                print("发送成功~~~~" + str(mssage))
              a=mssage
              time.sleep(10)#设置延迟时间
        except Exception as ex:
            print(str(ex))
if __name__ == "__main__":
    abc()
