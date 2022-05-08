import time
import random
import json
import requests
def dingdingjq(key, text):
    url = "https://oapi.dingtalk.com/robot/send?access_token="+key+""
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "text": {
            "content": "*ibox:\n"+text+""
        },
        "msgtype": "text"
    }
    print(requests.post(url=url, headers=headers, data=json.dumps(data)).json())
dingdingjq("f34079768b4ed89df7dafb42e35bd139943a7597fd406865509e6a102aa1780f",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+'--程序已退出')