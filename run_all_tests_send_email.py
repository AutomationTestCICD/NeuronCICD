from unittest import TestLoader


from HTMLTestRunner import HTMLTestRunner
import yagmail

suite = TestLoader().discover(r".", pattern='t0*.py') # 加载指定目录下的，符合指定模板格式的测试模块

with open("report.html", "wb") as f:
    r = HTMLTestRunner(stream=f, title="自动化接口测试", description=" 此次测试包含了主流程，以及各模块的增删改查") # 将测试运行器输出测试结果的目的地设置为f
    r.run(suite)
    
    
send = yagmail.SMTP("zhouxinwei@neurongenius.com", "2@2he0cmla7twtnq", "smtp.exmail.qq.com") # 构建一个邮件发送者对象
send.send("1020481340@qq.com", "自动生成测试报告调试", "自动化调试“勿回”", "report.html")