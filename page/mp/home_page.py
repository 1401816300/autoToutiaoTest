from selenium.webdriver.common.by import By
from base.mp.base_page import BasePage, BaseHandle

"""
自媒体端首页
"""
# 对象库层:将所有测试用例所需要在该页面操作的元素全部定义对应的实例方法找回来
class HomePage(BasePage):

    # 在初始化方法中定义元素的实例属性，并且赋值，值为定位方式以及定位方式的值
    def __init__(self):
        super().__init__()
        # 内容管理菜单栏
        self.content_manage = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章菜单栏
        self.pub_aritcal_manage = (By.XPATH, "//*[contains(text(),' 发布文章')]")

    def find_content_manage(self):
        return self.find_elt(self.content_manage)

    def find_pub_al_mg(self):
        return self.find_elt(self.pub_aritcal_manage)


# 操作层:通过调用对象库层的实例方法拿到元素对象，定义对应操作方法
class HomeHanle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    def click_content_mg(self):
        self.home_page.find_content_manage().click()

    def click_pub_al_mg(self):
        self.home_page.find_pub_al_mg().click()


# 业务层:调用多个操作层的实例方法就可以组织成对应的业务操作
class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHanle()

    # 跳转至发布文章页面
    def to_pub_ar_pg(self):
        self.home_handle.click_content_mg()
        self.home_handle.click_pub_al_mg()
