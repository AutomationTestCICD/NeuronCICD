'''
Created on 2019年10月30日

@author: zhouxinwei

备注：此模块提供基础的公共信息，比如被测服务器地址、公共头部等
'''
import time
import datetime

# 被测服务器地址
IP = "http://test.api.neurongenius.com"

# 公共头部
HEADERS = {'Accept': "application/json, text/plain, */*",
           'Accept-Encoding': "gzip, deflate",
           'Accept-Language': "zh-CN",
           'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Neuron-test/3.0.0 Chrome/80.0.3987.141 Electron/8.1.1 Safari/537.36",
           'Content-Type': "application/json;charset=UTF-8"}

# 定义账号信息
ADMIN_ACCOUNT = "188"
ADMIN_PASSWORD = "123456"

#定义当天开始时间和结束时间
today_start = time.strftime("%Y-%m-%d") +" 00:00:00"
today_end = time.strftime("%Y-%m-%d") +" 23:59:59"


Now_time =time.strftime("%Y-%m-%d %H:%M:%S")
Now_NextHours = (datetime.datetime.now()+datetime.timedelta(hours=0.5)).strftime("%Y-%m-%d %H:%M:%S")

# print(Now_time,Now_NextHours)