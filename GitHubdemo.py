import requests
api = 'https://oapi.dingtalk.com/robot/send?access_token=a1e70c2bba8848f0f1da5a84232538d5a58bff24cb3319ddea6974d50a55cf45'

r = requests.post(api, data={"msgtype": "text","text": {"content":"我就是我, 是不一样的烟火"}})
print(r.text)
