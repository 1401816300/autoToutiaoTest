import time
from page.mp.home_page import HomeProxy
from page.mp.publish_aritcal_page import PubAriProxy
from utils import DriverUtils, is_exists_element
import pytest

# 1.定义测试类
@pytest.mark.run(order=2)
class TestPubAritcal:
    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.pub_ari_proxy = PubAriProxy()

    # 3.定义测试方法
    def test_pub_artical(self):
        # 定义测试数据
        ari_title = "testCase_{}".format(time.strftime("%d%H%M%S"))
        ari_content = "我要出去找工作,找个好工作,月薪8W8,迎娶白富美！！！"
        option_name = "授课专用"
        # 调用业务层方法
        self.home_proxy.to_pub_ar_pg()
        self.pub_ari_proxy.test_pub_aritcal(ari_title, ari_content, option_name)
        # 执行断言
        assert is_exists_element(self.driver, "新增文章成功")

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
