from selenium import webdriver
from auto.CRM.Page.database import database
from selenium.webdriver. support.select import Select  # 导入模块


db = database()
# 定义关键字类

def open_browser(type_):
    # 定义driver的值，判断type是什么内容，则生成对应的浏览器对象即可
    try:
        driver = getattr(webdriver,type_)()
    except:
        driver = webdriver.Chrome()
    return driver

class webkeys:
    # 虚拟driver
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, type_):
        self.driver = open_browser(type_)

    # 访问url
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 元素定位
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 读取弹窗内容
    def alter_R(self):
        print(self.driver.switch_to.alert.text)

    # 点击弹窗确认键
    def alter_Y(self):
        self.driver.switch_to.alert.accept()

    # 输入
    def input_(self, name, value, text):
        self.locator(name, value).send_keys(text)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 转换frame
    def frame(self, value, i):
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name(value)[i])

    # 退出
    def quit(self):
        self.driver.quit()

    # 下拉菜单选择
    def select(self, name, value, text):
        se = self.locator(name, value)  # 选择婚姻
        Select(se).select_by_visible_text(text)


    def yzcare(self, sql):
        menu_table = self.locator("xpath", '/html/body/form/table/tbody/tr[2]/td[1]/div/table')
        rows = menu_table.find_elements_by_tag_name('tr')
        for i in range(2, len(rows)):
            print(rows[i].text)
        # python 得len()函数返回对象（字符、列表、元组）得长度或者元素得个数
        numbers = len(rows) - 2
        data = db.excute(sql)
        if data[0][0] == numbers:
            print('关怀提醒页面数量与数据库数量相同，测试成功')
        elif rows[2].text == '没有要关怀的对象！' and data[0][0] == numbers - 1:
            print('关怀提醒页面数量与数据库数量相同，测试成功')
        else:
            print('关怀提醒页面数量与数据库数量不同，测试失败')

    def yzbirth(self, sql):
        menu_table = self.locator("xpath", '/html/body/form/table/tbody/tr[4]/td[2]/div/table')
        rows = menu_table.find_elements_by_tag_name('tr')
        for i in range(2, len(rows)):
            print(rows[i].text)
        numbers = len(rows) - 2
        data = db.excute(sql)
        if data[0][0] == numbers:
            print('生日提醒页面数量与数据库数量相同，测试成功')
        elif rows[2].text == '没有要过生日的人！' and data[0][0] == numbers - 1:
            print('生日提醒页面数量与数据库数量相同，测试成功')
        else:
            print('生日提醒页面数量与数据库数量不同，测试失败')

    def yztalk(self, sql):
        menu_table = self.locator("xpath", '/html/body/form/table/tbody/tr[2]/td[2]/div/table')
        rows = menu_table.find_elements_by_tag_name('tr')
        for i in range(2, len(rows)):
            print(rows[i].text)
        numbers = len(rows) - 2
        data = db.excute(sql)
        if data[0][0] == numbers:
            print('联系提醒页面数量与数据库数量相同，测试成功')
        elif rows[2].text == '没有要联系的对象！' and data[0][0] == numbers - 1:
            print('联系提醒页面数量与数据库数量相同，测试成功')
        else:
            print('联系提醒页面数量与数据库数量不同，测试失败')




