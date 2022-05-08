import requests
import time
import json
import random
id = 0
idp = 0
noticeName = ''
noticeTime = ''
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
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN',
    'origin': 'https://www.ibox.art',
    'referer': 'https://www.ibox.art/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
} 
while True:
   try:
    ibox_gg = requests.get('https://api-h5.ibox.art/nft-mall-web/v1.2/nft/product/getCommonNoticeList?page=1&pageSize=20', headers=headers,timeout=10)
    x =ibox_gg.json()['data']['list']
    for i in x:
        odtim=time.strftime("%Y-%m-%d",time.localtime(int(str(i['noticeTime'])[0:10])))
        newtim =time.strftime("%Y-%m-%d",time.localtime())
        if odtim == newtim:
            id = int(i['id'])
            noticeName = i['noticeName']
            noticeTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(str(i['noticeTime'])[0:10])))
            break
    if id != idp:
        idp = id
        print(id,noticeName,noticeTime)
        s = "https://www.ibox.art/zh-cn/notice/detail/?id="+ str(id)
        dingdingjq("5d5c8147faffc1893727d22cbda1eb76a8a7729b9aba2e1d8ebd84c680951c1d",noticeName+'\n'+noticeTime+'\n'+s)
        ibox_gg.close()
        time.sleep(60 *random.randint(1,3))
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),'--未获取到新公告')
        ibox_gg.close()
        time.sleep(60 *random.randint(1,3))
   except:
       print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),'--网络错误')
       ibox_gg.close()  
