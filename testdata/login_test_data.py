'''
Created on 2019年10月30日

@author:zhouxinwei

备注：此模块提供测试登录接口时所需的测试数据
'''

LOGIN_TEST_DATA = [
    [{"account":"188","password":"nr123456"},"登陆成功"],
    [{"account":"188","password":"cuowu"},"账号或密码错误"],
    [{"account":"188","password":""},"密码不能为空"],
    [{"account":"","password":"nr123456"},"账号不能为空"],
    [{"account":"","password":""},"账号不能为空,密码不能为空"],
    ]