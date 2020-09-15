'''
Created on 2019年10月30日

@author: zhouxinwei

备注：此模块提供其他接口测试时需要的公共方法
'''
import requests
from common.interface_url import LOGIN_INTERFACE_URL
from common.base_info import HEADERS
from time import sleep

def get_headers_after_login():
    payload = '{"account":"188","password":"123456"}'
    headers = HEADERS.copy()
    response = requests.request("POST", LOGIN_INTERFACE_URL, data=payload, headers=headers)
    if  response.status_code in (502,500,401):
        print("\n服务器正在重启或异常") 
        times = input("重启进行中,请输入输入睡眠时间（秒）：")
        sleep(times) 

    else:
        # print("\n登陆成功")
        token = response.json()["data"]["user"]["token"]
        headers["Authorization"] = token
        # print(headers)
        return headers
    
def TestResult(response):
    
        print(f"响应对象的类型为：{type(response)}") 
        print(f"响应的协议状态码：{response.status_code}")
        print(f"响应协议状态码对应提示内容：{response.reason}")
        print(f"响应的头部信息：{response.headers}")
        print(f"响应数据的原始格式（HTTPResponse object）：{response.raw}")
        print(f"请求的地址：{response.url}") 
        print(f"响应内容的编码格式：{response.encoding}")
        print(f"响应的Cookie缓存信息：{response.cookies}")
        print(f"响应处理消耗的时间：{response.elapsed}")
        print(f"响应的文本内容：{response.text}")
        print(f"响应的字节码格式的内容：{response.content}")
        print(f"返回json格式的数据：{response.json()}")

# def get_last_notice_id():
#     # 得到登录后的头部，才能有访问权限
#     headers = get_headers_after_login()
#     response = requests.request("POST", NOTICE_QUERY_INTERFACE_URL, headers=headers)
#     last_notice_id = response.json()[0]["noticeid"]
# #     print(last_notice_id)
#     return int(last_notice_id), headers
#
# if __name__ == "__main__":
#     get_last_notice_id()