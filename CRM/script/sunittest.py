import unittest
from auto.CRM.script.CRMtestlogin import MyTestCase as aa
from auto.CRM.script.CRM工作台测试 import MyTestCase
from HTMLTestRunner import HTMLTestRunner #导入生成测试报告模块
import time
# 测试框架
suite = unittest.TestSuite()
suite.addTest(aa('test_login1'))
suite.addTest(aa('test_login2'))
suite.addTest(aa('test_login3'))
suite.addTest(aa('test_login4'))
suite.addTest(aa('test_login5'))
suite.addTest(aa('test_login6'))
suite.addTest(aa('test_login7'))
suite.addTest(MyTestCase('test_care1'))
suite.addTest(MyTestCase('test_care2'))
suite.addTest(MyTestCase('test_care3'))
suite.addTest(MyTestCase('test_care4'))
suite.addTest(MyTestCase('test_talk1'))
suite.addTest(MyTestCase('test_talk2'))
suite.addTest(MyTestCase('test_talk3'))
suite.addTest(MyTestCase('test_talk4'))
suite.addTest(MyTestCase('test_birth1'))
suite.addTest(MyTestCase('test_birth2'))
suite.addTest(MyTestCase('test_birth3'))
suite.addTest(MyTestCase('test_birth4'))
suite.addTest(MyTestCase('test_notice'))

# print(suite)
# # 测试执行
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 我们要新建一个用于保存我们测试结果的文件，html
now = time.strftime("%Y-%m-%d-%H-%M-%S")
print(now)
# 定义文件的名字
filename='./'+now+"_result.html"
print(filename)
file = open(filename, "wb")
# 执行我们的报告写入
runner=HTMLTestRunner(stream=file,title="CRM登录和工作台模块测试报告",description="用例执行情况:")
# stream：是指定测试报告文件
# title：指定报告的标题
# description:指定报告的副标题
# #执行我们测试用例
runner.run(suite)
time.sleep(3)
file.close()
