import unittest
import time
import os
from auto.CRM.Page.web_key import webkeys

f = os.path.abspath('../data/data.txt')
with open(f, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    a = []
    for line in lines:
        c = line.split('\n')
        b = c[0].split(',')
        a.append(b)

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('CRM登录自动化测试开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('CRM登录自动化测试结束')

    def setUp(self) -> None:
        self.wk = webkeys('Chrome')
        self.wk.open("http://localhost:8080/crm/")
        time.sleep(1)
        print('<---------------test start--------------->')


    def tearDown(self) -> None:
        time.sleep(1)
        print('<---------------test down---------------->')
        print('                                        ')
        self.wk.quit()


    def test_login1(self):
        '''账号密码都正确'''
        self.wk.input_('name', 'userNum',a[0][0])
        self.wk.input_('name','userPw',a[0][1])
        self.wk.click('id','in1')
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为',a[0][0],'密码为',a[0][1])
        else:
            print('登陆失败,用户名为',a[0][0],'密码为',a[0][1])

    def test_login2(self):
        '''账号为空，密码正确'''
        self.wk.input_('name','userNum',a[1][0])
        self.wk.input_('name','userPw',a[1][1])
        self.wk.click('id','in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[1][0], '密码为', a[1][1])
        else:
            print('登陆失败,用户名为', a[1][0], '密码为', a[1][1])

    def test_login3(self):
        '''账号正确，密码为空'''
        self.wk.input_('name', 'userNum', a[2][0])
        self.wk.input_('name', 'userPw', a[2][1])
        self.wk.click('id', 'in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[2][0], '密码为', a[2][1])
        else:
            print('登陆失败,用户名为', a[2][0], '密码为', a[2][1])

    def test_login4(self):
        '''账号密码都为空'''
        self.wk.input_('name', 'userNum', a[3][0])
        self.wk.input_('name', 'userPw', a[3][1])
        self.wk.click('id', 'in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[3][0], '密码为', a[3][1])
        else:
            print('登陆失败,用户名为', a[3][0], '密码为', a[3][1])

    def test_login5(self):
        '''账号错误，密码正确'''
        self.wk.input_('name', 'userNum', a[4][0])
        self.wk.input_('name', 'userPw', a[4][1])
        self.wk.click('id', 'in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[4][0], '密码为', a[4][1])
        else:
            print('登陆失败,用户名为', a[4][0], '密码为', a[4][1])

    def test_login6(self):
        '''账号正确，密码错误'''
        self.wk.input_('name', 'userNum', a[5][0])
        self.wk.input_('name', 'userPw', a[5][1])
        self.wk.click('id', 'in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[5][0], '密码为', a[5][1])
        else:
            print('登陆失败,用户名为', a[5][0], '密码为', a[5][1])

    def test_login7(self):
        '''账号密码都错误'''
        self.wk.input_('name', 'userNum', a[6][0])
        self.wk.input_('name', 'userPw', a[6][1])
        self.wk.click('id', 'in1')
        time.sleep(1)
        self.wk.alter_R()
        self.wk.alter_Y()
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为', a[6][0], '密码为', a[6][1])
        else:
            print('登陆失败,用户名为', a[6][0], '密码为', a[6][1])


if __name__ == '__main__':
    unittest.main()

