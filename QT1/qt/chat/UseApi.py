# 说明：将固定文本发送给百度平台实现UNIT的交流
import requests
import json
def Api(entstr):
    baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'  # 获取token的server
    grant_type = 'client_credentials'
    client_id = 'xzc2rLD2SsZRn5G2vCkB5rCX'  # API KEY
    client_secret = '2IY87wubtTe2IOEKYEqZDzTEGg7g3zmg'  # Secret KEY
    # 合成请求token的url
    url = baidu_server + 'grant_type=' + grant_type + '&client_id=' + client_id + '&client_secret=' + client_secret

    # 获取token
    res = requests.get(url).text
    data = json.loads(res)  # 将json格式转换为字典格式
    token = data['access_token']

    access_token = token
    q = entstr
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=' + access_token  # 不用动
    post_data = "{\"log_id\":\"UNITTEST_10000\",\"version\":\"2.0\",\"service_id\":\"S65015\",\"session_id\":\"\",\"request\":{\"query\":\"%s\",\"user_id\":\"88888\",\"query_info\":{\"type\":\"TEXT\",\"source\":\"KEYBOARD\"}}}}" % (
        q)

    headers = {'content-type': 'application/x-www-form-urlencoded'}  # 不用管
    response = requests.post(url, data=post_data.encode('utf-8'), headers=headers)

    if response:
        r = response.json()
        saying = r["result"]["response_list"][1]["action_list"][0]["say"]  # 擦，这个json层级真难找。。

    return saying