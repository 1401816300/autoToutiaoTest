from selenium.webdriver.common.by import By
from base.mp.base_page import BasePage, BaseHandle

"""
自媒体端登陆页面
"""
# 对象库层:将所有测试用例所需要在该页面操作的元素全部定义对应的实例方法找回来
class LoginPage(BasePage):

    # 在初始化方法中定义元素的实例属性，并且赋值，值为定位方式以及定位方式的值
    def __init__(self):
        super().__init__()
        # 手机号码
        self.phone_num = (By.CSS_SELECTOR, "[placeholder*='手机']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder*='验证码']")
        # 登陆按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_phone_num(self):
        return self.find_elt(self.phone_num)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层:通过调用对象库层的实例方法拿到元素对象，定义对应操作方法
class LoginHanle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号码
    def input_phone(self, phone):
        self.input_text(self.login_page.find_phone_num(), phone)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登陆按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层:调用多个操作层的实例方法就可以组织成对应的业务操作
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHanle()

    # 登陆业务
    def test_login(self, phone, code):
        self.login_handle.input_phone(phone)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
