from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtils


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # 账号
        self.username = (By.NAME, "username")
        # 密码
        self.password = (By.NAME, "password")
        # 登陆
        self.submit_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, usr):
        self.input_text(self.login_page.find_username(), usr)

    # 输入密码
    def input_password(self, pwd):
        self.input_text(self.login_page.find_password(), pwd)

    # 点击登陆按钮
    def click_submit_btn(self):
        js_str = 'document.getElementById("inp1").removeAttribute("disabled")'
        DriverUtils.get_mis_driver().execute_script(js_str)
        self.login_page.find_submit_btn().click()


# 业务层
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # MIS登陆方法
    def test_mis_login(self, usr, pwd):
        self.login_handle.input_username(usr)
        self.login_handle.input_password(pwd)
        self.login_handle.click_submit_btn()
