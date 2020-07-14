"""发布文章页面"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


# 对象库层:将所有测试用例所需要在该页面操作的元素全部定义对应的实例方法找回来
class PubAriPage(BasePage):

    # 在初始化方法中定义元素的实例属性，并且赋值，值为定位方式以及定位方式的值
    def __init__(self):
        super().__init__()
        # 文章标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder*='名称']")
        # iframe
        self.cont_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.ari_content = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道
        self.channel = (By.CSS_SELECTOR, "[placeholder*='请选择']")
        # 频道的选项
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    def find_cont_iframe(self):
        return self.find_elt(self.cont_iframe)

    def find_ari_content(self):
        return self.find_elt(self.ari_content)

    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_channel_op(self):
        return self.find_elt(self.channel_option)

    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层:通过调用对象库层的实例方法拿到元素对象，定义对应操作方法
class PubAriHandle(BaseHandle):

    def __init__(self):
        self.pub_ari_page = PubAriPage()

    # 输入文章标题
    def input_ari_title(self, title):
        self.input_text(self.pub_ari_page.find_ari_title(), title)

    # 输入文章内容
    def input_ari_content(self, content):
        # iframe切换
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_ari_page.find_cont_iframe())
        self.input_text(self.pub_ari_page.find_ari_content(), content)
        # 返回默认页面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def check_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    # 选择频道
    def check_target_channel(self, option_name):
        select_option("请选择", option_name)

    # 点击发表
    def click_pub_btn(self):
        self.pub_ari_page.find_pub_btn().click()


# 业务层:调用多个操作层的实例方法就可以组织成对应的业务操作
class PubAriProxy:

    def __init__(self):
        self.pub_ari_handle = PubAriHandle()

    # 发表文章
    def test_pub_aritcal(self, title, content, option_name):
        # 1.输入标题
        self.pub_ari_handle.input_ari_title(title)
        # 2.输入内容
        self.pub_ari_handle.input_ari_content(content)
        # 3.选择封面
        self.pub_ari_handle.check_cover()
        # 4.选择频道
        self.pub_ari_handle.check_target_channel(option_name)
        # 5.点击发表
        self.pub_ari_handle.click_pub_btn()
