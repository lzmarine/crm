import unittest
import time
from auto.CRM.Page.web_key import webkeys
from auto.CRM.Page.database import database
from auto.CRM.Page.base import Base
import pytest

db = database()
b = Base()
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('CRM添加员工自动化测试开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('CRM添加员工自动化测试结束')

    def setUp(self) -> None:
        print('---------------test start---------------')
        self.wk = webkeys('Chrome')
        self.wk.open("http://localhost:8080/crm/")
        self.wk.input_('name', 'userNum', 'admin')
        self.wk.input_('name', 'userPw', '123456')
        self.wk.click('id', 'in1')
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为admin,密码为123456')
        else:
            print('登陆失败,用户名为admin,密码为123456')
        self.wk.frame('frame', 1)
        self.wk.click('xpath', '//*[@id="imgmenu4"]/table/tbody/tr/td[2]')
        time.sleep(1)
        self.wk.click('xpath', '//*[@id="submenu4"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a')
        time.sleep(2)
        self.wk.driver.switch_to.default_content()
        self.wk.frame('frame', 2)

    def tearDown(self) -> None:
        print('---------------test down----------------')
        print('                                        ')
        self.wk.quit()

    @pytest.mark.tryfirst
    def test_work0(self):
        self.wk.input_('name', 'userName', b.name())  # 输入姓名
        self.wk.input_('name', 'userAge', b.age())  # 输入年龄
        time.sleep(1)
        self.wk.select('name', 'userSex', b.sex())
        time.sleep(1)
        self.wk.select('name', 'userDiploma', b.education())
        self.wk.select('name', 'departmentId', b.department())
        time.sleep(1)
        self.wk.input_('name', 'userTel', b.zjphone())  # 输入座机
        self.wk.input_('name', 'userBankcard', b.bankid())  # 输入工资卡号
        c = b.idcard()
        self.wk.input_('name', 'userIdnum', c)  # 输入身份证
        self.wk.driver.switch_to.default_content()  # 查找当前登录的用户名字
        self.wk.frame('frame', 0)
        user = self.wk.locator('xpath', '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
        add = str(user).split('：')[1]
        self.wk.driver.switch_to.default_content()  # 输入添加人
        self.wk.frame('frame', 2)
        self.wk.input_('name', 'userAddman', add)
        self.wk.input_('name', 'userNum', b.usernum())  # 输入账号
        self.wk.input_('name', 'userPw', b.usernum())  # 输入密码
        self.wk.input_('name','userNation', b.nation())  # 输入民族
        time.sleep(1)
        self.wk.select('name', 'isMarried', b.marry())  # 选择婚姻状况
        time.sleep(1)
        self.wk.select('name', 'roleId', b.role())  # 选择角色
        self.wk.input_('name', 'userIntest', b.habit())  # 输入爱好
        self.wk.input_('name', 'userMobile', b.phone())  # 输入手机号
        self.wk.input_('name', 'userAddress', b.address())  # 输入地址
        self.wk.input_('name', 'userEmail', b.email())  # 输入邮件地址
        time.sleep(1)
        self.wk.click('name', 'submit')
        time.sleep(2)
        self.wk.alter_Y()
        d = db.excute("SELECT user_idnum FROM user_info WHERE user_idnum={};".format(c))
        if d[0][0] == c:
            print('添加员工成功')
        else:
            print('添加员工失败')




if __name__ == '__main__':
    unittest.main()





