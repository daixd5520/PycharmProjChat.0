#todo:调按钮在整个界面
#2022.4.7:目前可以图形化界面单独运行智能对话+餐饮推荐
import math
import json
import requests
import numpy as np
import random


def loadData():
    f = open(r'.\data\u.data')  ##user id | food id | rating | timestamp
    data = []
    for i in range(100000):
        h = f.readline().split('\t')
        h = list(map(int, h))
        data.append(h[0:3])
    f.close()
    return data


def loadFoodName():  # ISO-8859-1
    f = open(r'E:\大创5人\交互界面2.0\QT1\qt\chat\data\u.item.txt', encoding='utf-8')  ##food id | food name | finish date | sell date | IMDb URL(删) |
    # unknown | Baicai | Bean | Beef | Bocai | Carrot | Chicken | Duck | Fish |
    # Guangdong | Jiangsu | Jinzhengu | Mushroom | Pork | Shandong | Sichuan | Spicy | Sweet | Sour  #(后19个是菜品标签)#
    name = []
    for i in range(1682):
        h = f.readline()
        k = ''
        m = 0
        for j in range(100):
            k += str(h[j])
            if str(h[j]) == '|':
                m += 1
            if m == 2:
                break
        name.append(k)
    f.close()
    return name


def manageDate(data):
    outdata = []
    for i in range(943):
        outdata.append([])
        for j in range(1682):
            outdata[i].append(0)
    for h in data:
        outdata[h[0] - 1][h[1] - 1] = h[2]
    return outdata


def calcMean(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)
    x_mean = float(sum_x + 0.0) / n
    y_mean = float(sum_y + 0.0) / n
    return x_mean, y_mean


def calcPearson(x, y):
    x_mean, y_mean = calcMean(x, y)  # 计算x,y向量平均值
    n = len(x)
    sumTop = 0.0
    sumBottom = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(n):
        sumTop += (x[i] - x_mean) * (y[i] - y_mean)
    for i in range(n):
        x_pow += math.pow(x[i] - x_mean, 2)
    for i in range(n):
        y_pow += math.pow(y[i] - y_mean, 2)
    sumBottom = math.sqrt(x_pow * y_pow)
    p = sumTop / sumBottom
    return p


def calcAttribute(dataSet, num):
    prr = []
    n, m = np.shape(dataSet)  # 获取数据集行数和列数
    x = [0] * m  # 初始化特征x和类别y向量
    y = [0] * m
    y = dataSet[num - 1]
    for j in range(n):  # 获取每个特征的向量，并计算Pearson系数，存入到列表中
        x = dataSet[j]
        prr.append(calcPearson(x, y))
    return prr


def choseFood(outdata, num):
    prr = calcAttribute(outdata, num)
    list = []
    mid = []
    out_list = []
    movie_rank = []
    for i in range(1682):
        movie_rank.append([i, 0])
    k = 0
    for i in range(943):
        list.append([i, prr[i]])
    for i in range(943):
        for j in range(942 - i):
            if list[j][1] < list[j + 1][1]:
                mid = list[j]
                list[j] = list[j + 1]
                list[j + 1] = mid
    for i in range(1, 51):
        for j in range(0, 1682):
            movie_rank[j][1] = movie_rank[j][1] + outdata[list[i][0]][j] * list[i][1] / 50
    for i in range(1682):
        for j in range(1681 - i):
            if movie_rank[j][1] < movie_rank[j + 1][1]:
                mid = movie_rank[j]
                movie_rank[j] = movie_rank[j + 1]
                movie_rank[j + 1] = mid
    for i in range(1, 1682):
        if (outdata[num - 1][movie_rank[i][0]] == 0):
            mark = 0
            for d in out_list:
                if d[0] == j:
                    mark = 1
                if mark != 1:
                    k += 1
                    out_list.append(movie_rank[i])
            if k == 10:
                break
    return movie_rank


def printFood(out_list, name):
    # print(">>小Q:\n为您专门推荐以下菜品:(编号 | 菜名 |)")
    s = ">>小Q:\n为您专门推荐以下菜品:(编号 | 菜名 |)\n"
    for i in range(10):
        # print(name[out_list[i][0]]," rank score:",out_list[i][1])
        # print(name[out_list[i][0]])
        s = s + (name[out_list[i][0]] + "\n")
    return s


def apiUsing(entstr):
    baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'  # 获取token的server
    grant_type = 'client_credentials'
    client_id = 'xzc2rLD2SsZRn5G2vCkB5rCX'  # API KEY
    client_secret = '2IY87wubtTe2IOEKYEqZDzTEGg7g3zmg'  # Secret KEY2IY87wubtTe2IOEKYEqZDzTEGg7g3zmg
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
    # print(">>小Q:")
    print(saying)
    s = ">>小Q:"
    s += saying
    return s


def myChat():
    i_data = loadData()
    name = loadFoodName()
    out_data = manageDate(i_data)
    a = random.randint(0, 1500)
    # print("a=")
    # print(a)
    # if(a<=1500):
    out_list = choseFood(out_data, a)
    s = printFood(out_list, name)
    # print("myChat中的s:")
    # print(s)
    # else:
    #     print("对不起,您输入的用户不存在哦!")
    return s


def getRes(entstr):
    lst = ["推荐", "好吃", "饭", "菜"]
    # byeLst = ["拜拜", "不聊了", "不说了", "再见"]
    mystr = entstr
    canUseMine = -1
    for name in lst:
        if name in mystr:
            canUseMine = 1
            break
    if (canUseMine == 1):
        s = myChat()
    else:
        s = apiUsing(mystr)
    return s
