import unittest
import time
from selenium.webdriver. support.select import Select#导入模块
from auto.CRM.Page.web_key import webkeys
from auto.CRM.Page.database import database

db=database()

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('CRM工作台自动化测试开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('CRM工作台自动化测试结束')

    def setUp(self) -> None:
        print('---------------test start---------------')
        self.wk = webkeys('Chrome')
        self.wk.open("http://localhost:8080/crm/")
        time.sleep(1)
        self.wk.input_('name', 'userNum', 'admin')
        self.wk.input_('name', 'userPw', '123456')
        self.wk.click('id', 'in1')
        time.sleep(1)
        if self.wk.driver.current_url == 'http://localhost:8080/crm/servlet/LoginCheckServlet':
            print('登陆成功,用户名为admin,密码为123456')
        else:
            print('登陆失败,用户名为admin,密码为123456')

    def tearDown(self) -> None:
        print('---------------test down----------------')
        print('                                        ')
        self.wk.quit()

    def test_care1(self):#查询当天的关怀提醒
        '''查询当天的关怀提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime')
        Select(se).select_by_visible_text('当天')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div1"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzcare("SELECT count(1) FROM customer_care WHERE MONTH(care_nexttime) = MONTH(NOW()) and DAY(care_nexttime) = DAY(NOW())")


    def test_care2(self):#查询一周内的关怀提醒
        '''查询一周内的关怀提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime')
        Select(se).select_by_visible_text('一周内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div1"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzcare("SELECT count(1) FROM customer_care WHERE date_format( care_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 7 DAY ) , '%m%d' )")


    def test_care3(self):#查询半月内的关怀提醒
        '''查询半月内的关怀提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime')
        Select(se).select_by_visible_text('半月内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div1"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzcare("SELECT count(1) FROM customer_care WHERE date_format( care_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 15 DAY ) , '%m%d' )")


    def test_care4(self):#查询一月内的关怀提醒
        '''查询一月内的关怀提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime')
        Select(se).select_by_visible_text('一月内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div1"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzcare("SELECT count(1) FROM customer_care WHERE date_format( care_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 30 DAY ) , '%m%d' )")


    def test_birth1(self):#查询当天的生日提醒
        '''查询当天的生日提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime2')
        Select(se).select_by_visible_text('当天')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzbirth("SELECT count(1) FROM customer_info WHERE MONTH(birth_day) = MONTH(NOW()) and DAY(birth_day) = DAY(NOW())")


    def test_birth2(self):#查询一周内的生日提醒
        '''查询一周内的生日提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime2')
        Select(se).select_by_visible_text('一周内')
        time.sleep(1)
        self.wk.locator("xpath", '//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzbirth("SELECT count(1) FROM customer_info WHERE date_format( birth_day,'%m%d')  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 7 DAY ) , '%m%d' )")


    def test_birth3(self):#查询半月内的生日提醒
        '''查询半月内的生日提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime2')
        Select(se).select_by_visible_text('半月内')
        time.sleep(1)
        self.wk.locator("xpath", '//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzbirth("SELECT count(1) FROM customer_info WHERE date_format( birth_day,'%m%d')  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 15 DAY ) , '%m%d' )")


    def test_birth4(self):#查询一月内的生日提醒
        '''查询一月内的生日提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime2')
        Select(se).select_by_visible_text('一月内')
        time.sleep(1)
        self.wk.locator("xpath", '//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yzbirth("SELECT count(1) FROM customer_info WHERE date_format( birth_day,'%m%d')  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 30 DAY ) , '%m%d' )")

    def test_talk1(self):#查询当天的联系提醒
        '''查询当天的联系提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime1')
        Select(se).select_by_visible_text('当天')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yztalk("SELECT count(1) FROM customer_linkreord WHERE MONTH(link_nexttime) = MONTH(NOW()) and DAY(link_nexttime) = DAY(NOW())")


    def test_talk2(self):#查询一周内的联系提醒
        '''查询一周内的联系提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime1')
        Select(se).select_by_visible_text('一周内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yztalk("SELECT count(1) FROM customer_linkreord WHERE date_format(link_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 7 DAY ) , '%m%d' )")


    def test_talk3(self):#查询半月内的联系提醒
        '''查询半月内的联系提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime1')
        Select(se).select_by_visible_text('半月内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yztalk("SELECT count(1) FROM customer_linkreord WHERE date_format(link_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 15 DAY ) , '%m%d' )")


    def test_talk4(self):#查询一月内的联系提醒
        '''查询一月内的联系提醒'''
        self.wk.frame('frame',2)
        se = self.wk.locator('name','addTime1')
        Select(se).select_by_visible_text('一月内')
        time.sleep(1)
        self.wk.locator("xpath",'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input').click()
        time.sleep(1)
        self.wk.yztalk("SELECT count(1) FROM customer_linkreord WHERE date_format(link_nexttime, '%m%d' )  BETWEEN date_format( now( ) , '%m%d' ) AND date_format( date_add( now( ) , INTERVAL 30  DAY ) , '%m%d' )")


    def test_notice(self):#查询有效公告信息
        '''查询有效公告信息'''
        self.wk.frame('frame',2)
        data = db.excute("SELECT count(1) FROM notice_info WHERE MONTH(notice_endtime) = MONTH(NOW()) and DAY(notice_endtime) > DAY(NOW())")
        menu_table = self.wk.locator("xpath",'/html/body/form/table/tbody/tr[4]/td[1]/div/table')
        rows = menu_table.find_elements_by_tag_name('tr')
        for i in range(1, len(rows)):
            print(rows[i].text)
        numbers = len(rows) - 1
        if data[0][0] == numbers:
            print('有效公告页面数量与数据库数量相同，测试成功')
        elif rows[1].text == '没有有效的公告！' and data[0][0] == numbers-1:
            print('有效公告页面数量与数据库数量相同，测试成功')
        else:
            print('有效公告页面数量与数据库数量不同，测试失败')


if __name__ == '__main__':
    unittest.main()




