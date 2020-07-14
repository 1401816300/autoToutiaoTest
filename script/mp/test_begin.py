from utils import DriverUtils
import pytest


@pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        # 修改关闭浏览器的开关值为False
        DriverUtils.change_mp_key(False)
