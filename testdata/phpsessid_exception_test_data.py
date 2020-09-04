'''
Created on 2019年10月30日

@author:zhouxinwei

备注：此模块提供测试添加公告接口时所需的测试数据
'''
from time import time
from common.common_method import get_last_notice_id

PHPSESSID_EXCEPTION_TEST_DATA = [
    ["PHPSESSID=", "没有访问权限"],
    ["", "没有访问权限"],
    ["PHPSESSID=804480000b6e000084ebb78c000000000", "没有访问权限"],
    ]