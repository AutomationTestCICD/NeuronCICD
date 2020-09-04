'''
Created on 2020年8月11日

@author: Administrator
'''
import unittest, requests
from common.base_info import today_start, today_end, Now_time,\
    Now_NextHours
from common.common_method import get_headers_after_login, TestResult
from common.interface_url import bespeakList_INTERFACE_URL,\
    bespeak_ADD_INTERFACE_URL
 

login_headers = get_headers_after_login()

class TestBespeak(unittest.TestCase):
    '''测试【预约】类'''

    def setUp(self):
        
        self.url01 = bespeak_ADD_INTERFACE_URL
        self.url02 = bespeakList_INTERFACE_URL

    def tearDown(self):
        pass
    
    def test_bespeak01(self):
        '''测试新增预约''' 
        
        data = '{"startTime":"%s","endTime":"%s","purpose":"%s 新建的","expertId":"309145a7791687cb20e5710cecdb3f0b","expertName":"NGTest","customerName":"NG勿删","customerId":"d6f50a1a2492f9c8f910180b3ed6d267","bespeakTypeValue":"1","bespeakTypeName":"咨询","bespeakTypeColor":"#98d8a6","inviteId":"309145a7791687cb20e5710cecdb3f0b","inviteName":"NGTest","bespeakUserId":"309145a7791687cb20e5710cecdb3f0b","bespeakUserName":"NGTest","bespeakProject":[{"dataType":1,"dataId":"634651eccc097e739e55fea5505c9520","dataName":"勿删分类"}]}'  %(Now_time,Now_NextHours,Now_time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       )
        response = requests.request("POST", self.url01, data=data.encode("utf-8"), headers=login_headers)
#         print(response.text)

        self.assertEqual("新建预约成功", response.json()["msg"], "----新建预约失败")
        print("新建预约成功\n")
    
    def test_bespeak02(self):
        '''测试预约列表''' 
        
        data = '{"index":1,"size":15,"startTime":"%s","endTime":"%s","getTotalFlag":true}'  %(today_start,today_end)
        response = requests.request("POST", self.url02, data=data, headers=login_headers)  
        TestResult(response)
        print(f'\n************今日目前总计{response.json()["data"]["total"]}条预约数据************')
    
#     #     对应  遍历值、项（返回列表） key、value、item
#     #     遍历出字典的内容
#         dict = response.json()["data"]
#         for key in dict.keys():
#             print(key + ':' + str(dict[key]))
#         input()
        self.assertIn("成功获取数据，数据非空", response.json()["msg"],"未获取到数据")
        
    def test_bespeak03(self):
        '''测试预约编辑''' 
        pass
    
    def test_bespeak04(self):
        '''测试预约删除''' 
        pass            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    

        