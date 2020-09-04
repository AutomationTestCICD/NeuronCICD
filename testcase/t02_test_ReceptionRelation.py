'''
Created on 2020年8月11日

@author: Administrator
'''

import unittest, requests
from common.base_info import today_start, today_end
from common.common_method import get_headers_after_login, TestResult
from common.interface_url import receptionList_INTERFACE_URL
 

login_headers = get_headers_after_login()

class TestReception(unittest.TestCase):
    '''测试【接待】类'''

    def setUp(self):
        
        self.url02 = receptionList_INTERFACE_URL

    def tearDown(self):
        pass
    
    def test_reception01(self):
        '''测试新增接待''' 
        pass        
    
    def test_reception02(self):
        '''测试接待列表''' 
        
        data = '{"startTime":"%s","endTime":"%s","index":1,"size":20,"autoFlag":null,"getTotalFlag":true}' %(today_start,today_end) 
        response = requests.request("POST", self.url02, data=data, headers=login_headers)  
        TestResult(response) 
        print(f'\n************今日目前总计{response.json()["data"]["total"]}条接待数据************')
        self.assertIn("成功获取数据，数据非空", response.json()["msg"],"未获取到数据")
   
#     #     对应  遍历值、项（返回列表） key、value、item
#     #     遍历出字典的内容
#         dict = response.json()["data"]
#         for key in dict.keys():
#             print(key + ':' + str(dict[key]))
#         input()
        
    def test_reception03(self):
        '''测试接待编辑''' 
        pass
    
    def test_reception04(self):
        '''测试接待删除''' 
        pass            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    

        