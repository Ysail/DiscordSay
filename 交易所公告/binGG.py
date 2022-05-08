from requests_html import HTMLSession
from time import sleep
import requests
import json
session = HTMLSession()


def dingdingjq(key, text):
    url = "https://oapi.dingtalk.com/robot/send?access_token="+key+""
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "text": {
            "content": "BSC:\n"+text+""
        },
        "msgtype": "text"
    }
    print(requests.post(url=url, headers=headers, data=json.dumps(data)).json())
def reqs():
    req = session.get('https://www.binance.com/en/support/announcement/')
    r= req.html.search('Binance Will List {} ({})')
    return r[1]
r0 = reqs()
print("r0",r0)
while True:
    sleep(1)
    r1 = reqs()
    print("r1",r1)
    if r0 != r1:
        for i in range(10):
            dingdingjq("0c78d4511bcb45dc302721828279c9a20efa968a66c4dc7a52a86095b52f11e1", "("+r1+") :币安新币")
    r0 = r1