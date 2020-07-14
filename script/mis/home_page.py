from selenium.webdriver.common.by import By
from base.mis.base_page import BasePage, BaseHandle

class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        # 信息管理
        self.info_mg = (By.XPATH, "//*[text()='信息管理']")
        # 内容审核
        self.content_mg = (By.XPATH, "//*[text()='内容审核']")

    def find_info_mg(self):
        return self.find_elt(self.info_mg)

    def find_content_mg(self):
        return self.find_elt(self.content_mg)


class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    # 点击信息管理
    def click_info_mg(self):
        self.home_page.find_info_mg().click()

    # 点击内容审核
    def click_content_mg(self):
        self.home_page.find_content_mg().click()


class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 去审核内容页面
    def to_aduit_page(self):
        self.home_handle.click_info_mg()
        self.home_handle.click_content_mg()
