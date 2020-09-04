'''
Created on 2019年10月30日

@author:zhouxinwei
'''
import unittest, requests
from ddt import ddt, data, unpack
from testdata.login_test_data import LOGIN_TEST_DATA
from common.interface_url import LOGIN_INTERFACE_URL
from common.base_info import HEADERS

@ddt
class TestLoginWithDDT(unittest.TestCase):
    
    @data(*LOGIN_TEST_DATA)
    @unpack
    def test_01(self, data, expect_result):
        response = requests.request("POST", LOGIN_INTERFACE_URL, data=data, headers=HEADERS)
        self.assertEqual(expect_result, response.json()["msg"])


        