from utils import DriverUtils
import pytest


@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 修改关闭浏览器驱动的值为Ture
        DriverUtils.change_mp_key(True)
        DriverUtils.quit_mp_driver()
