from utils import DriverUtils


# 对象库层基类
class BasePage:

    def __init__(self):
        # 获取自媒体端的浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()

    # 公用的定位元素的方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 操作层基类
class BaseHandle:

    # 模拟输入的公用方法,元素对象,模拟输入的文本
    def input_text(self, element, text):
        """
        :param element: 元素对象
        :param text: 模拟输入的文本
        :return:
        """
        element.clear()
        element.send_keys(text)
