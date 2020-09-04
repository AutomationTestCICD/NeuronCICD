'''
Created on 2019年10月30日

@author: zhouxinwei

备注：此模块提供测试添加公告接口时所需的测试数据
'''
from time import time
from common.common_method import get_last_notice_id

NOTICE_ADD_TEST_DATA = [
    [{"headline":"公告标题"+str(time()),"content":"公告内容"+str(time()),"scope":"1","expireddate":"2020-04-14"}, get_last_notice_id],
    [{"headline":"","content":"公告内容"+str(time()),"scope":"1","expireddate":"2020-04-14"}, "公告标题不能为空"],
    [{"content":"公告内容"+str(time()),"scope":"1","expireddate":"2020-04-14"}, "缺少必填参数：公告标题"],
    ]