'''
Created on 2019年10月30日

@author: zhouxinwei
'''
import unittest, requests
from common.base_info import today_start, today_end
from common.common_method import get_headers_after_login, TestResult
from common.interface_url import bespeakList_INTERFACE_URL,\
    receptionList_INTERFACE_URL


login_headers = get_headers_after_login()

class TestMain(unittest.TestCase):
    '''测试主流程'''
    def setUp(self):
        print("*************************************************************************************")
        self.url01 = bespeakList_INTERFACE_URL
        self.url02 = receptionList_INTERFACE_URL

    def tearDown(self):
        pass
     
    def test_bespeak01(self):
        '''测试预约列表''' 
        
        data = '{"index":1,"size":15,"startTime":"%s","endTime":"%s","getTotalFlag":true}'  %(today_start,today_end)
        response = requests.request("POST", self.url01, data=data, headers=login_headers)  
        TestResult(response)
        print(f'\n************今日目前总计{response.json()["data"]["total"]}条预约数据************')
    
#     #     对应  遍历值、项（返回列表） key、value、item
#     #     遍历出字典的内容
#         dict = response.json()["data"]
#         for key in dict.keys():
#             print(key + ':' + str(dict[key]))
#         input()

        self.assertIn("成功获取数据，数据非空", response.json()["msg"],"未获取到数据")
             
    def test_reception01(self):
        '''测试接待列表'''          
        
        data = '{"startTime":"%s","endTime":"%s","index":1,"size":20,"autoFlag":null,"getTotalFlag":true}' %(today_start,today_end) 
        response = requests.request("POST", self.url02, data=data, headers=login_headers)  
        TestResult(response) 
        print(f'\n************今日目前总计{response.json()["data"]["total"]}条接待数据************')
        self.assertIn("成功获取数据，数据非空", response.json()["msg"],"未获取到数据")

  

            
    # 以此类推，可以将所有的测试用例一一转化为上述的test方法
        