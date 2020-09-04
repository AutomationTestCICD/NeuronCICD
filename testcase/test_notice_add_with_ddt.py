'''
Created on 2019年10月30日

@author:zhouxinwei
'''
import unittest, requests
from ddt import ddt, data, unpack
from testdata.notice_add_test_data import NOTICE_ADD_TEST_DATA
from common.common_method import get_last_notice_id,\
    get_headers_after_login
from common.interface_url import NOTICE_ADD_INTERFACE_URL
from testdata.phpsessid_exception_test_data import PHPSESSID_EXCEPTION_TEST_DATA
from common.base_info import HEADERS

@ddt
class TestNoticeAddWithDDT(unittest.TestCase):
    
    @data(*NOTICE_ADD_TEST_DATA)
    @unpack
    def test_normal(self, data, expect_result):
        # 判断期望结果是否为动态的
        if expect_result is get_last_notice_id:
            last_notice_id, headers = get_last_notice_id()
            expect_result = str(last_notice_id + 1)
        else:
            headers = get_headers_after_login()
        response = requests.request("POST", NOTICE_ADD_INTERFACE_URL, data=data, headers=headers)
        self.assertEqual(expect_result, response.text)

    @data(*PHPSESSID_EXCEPTION_TEST_DATA)
    @unpack
    def test_phpsessid_exception(self, phpsessid, expect_result):
        # 定义测试数据
        data = NOTICE_ADD_TEST_DATA[0][0]
        # 判断期望结果是否为动态的
        headers = HEADERS.copy()
        headers["Cookie"] = phpsessid
        response = requests.request("POST", NOTICE_ADD_INTERFACE_URL, data=data, headers=headers)
        self.assertEqual(expect_result, response.text)
        