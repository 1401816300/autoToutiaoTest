import time

from page.mis.login_page import LoginProxy
from utils import DriverUtils, is_exists_element


class TestLogin:

    # 1.创建驱动对象以及打开浏览器
    # 2.创建测试方法所要调用的业务方法所在类的对象
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_proxy = LoginProxy()

    # 1.定义测试数据
    # 2.执行测试用例操作步骤
    # 3.执行断言
    def test_login(self):
        username = "testid"
        password = "testpwd123"

        self.login_proxy.test_mis_login(username, password)

        assert is_exists_element(self.driver, "管理员")

    # 1.释放测试资源
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()
