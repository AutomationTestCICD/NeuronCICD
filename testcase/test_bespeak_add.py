'''
Created on 2019年10月30日

@author:zhouxinwei
'''
import unittest, requests
from common.interface_url import bespeak_ADD_INTERFACE_URL
from common.base_info import Now_time, Now_NextHours
from testcase.t00_test_Main import login_headers
# from time import time
# from common.common_method import get_last_notice_id,\
#     get_headers_after_login



class TestBespeakAdd(unittest.TestCase):
    '''测试新增预约'''
    def setUp(self):
        self.url = bespeak_ADD_INTERFACE_URL
     
     
    @unittest.skip("我想跳过新增预约")   
    def test_01(self):
        data = '{"startTime":"%s","endTime":"%s","purpose":"%s 新建的","expertId":"309145a7791687cb20e5710cecdb3f0b","expertName":"NGTest","customerName":"NG勿删","customerId":"d6f50a1a2492f9c8f910180b3ed6d267","bespeakTypeValue":"1","bespeakTypeName":"咨询","bespeakTypeColor":"#98d8a6","inviteId":"309145a7791687cb20e5710cecdb3f0b","inviteName":"NGTest","bespeakUserId":"309145a7791687cb20e5710cecdb3f0b","bespeakUserName":"NGTest","bespeakProject":[{"dataType":1,"dataId":"634651eccc097e739e55fea5505c9520","dataName":"勿删分类"}]}'  %(Now_time,Now_NextHours,Now_time)
        response = requests.request("POST", self.url, data=data.encode("utf-8"), headers=login_headers)
#         print(response.text)
        self.assertEqual("新建预约成功", response.json()["msg"], "----新建预约失败")

#     def test_01(self):
#         # 定义测试数据
#         data = {
#             "headline":"公告标题"+str(time()),
#             "content":"公告内容"+str(time()),
#             "scope":"1",
#             "expireddate":"2020-04-14"
#             }
#         # 得到最后的公告id
#         last_notice_id, headers = get_last_notice_id()
#         # 模拟进行发包
#         response = requests.request("POST", self.url, data=data, headers=headers)
#         print(response.text)
#         self.assertEqual(last_notice_id+1, int(response.text))
# 
#     def test_02(self):
#         # 定义测试数据
#         data = {
#             "headline":"",
#             "content":"公告内容"+str(time()),
#             "scope":"1",
#             "expireddate":"2020-04-14"
#             }
#         # 得到登录后的头部信息
#         headers = get_headers_after_login()
#         # 模拟进行发包
#         response = requests.request("POST", self.url, data=data, headers=headers)
#         self.assertEqual("公告标题不能为空", response.text)
#     
#     def test_03(self):
#         # 定义测试数据
#         data = {
#             "content":"公告内容"+str(time()),
#             "scope":"1",
#             "expireddate":"2020-04-14"
#             }
#         # 得到登录后的头部信息
#         headers = get_headers_after_login()
#         # 模拟进行发包
#         response = requests.request("POST", self.url, data=data, headers=headers)
#         self.assertEqual("缺少必填参数：公告标题", response.text)
#     
#     # 以此类推，可以将所有的测试用例一一转化为上述的test方法
        