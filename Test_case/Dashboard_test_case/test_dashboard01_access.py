import unittest
from arize_auto_test.serves.common_serves import *
from arize_auto_test.serves.dashboard_serves import *
from arize_auto_test.serves.common_Method import *

name = open_yaml_data("test_data")["common_id"]["name"]
pw = open_yaml_data("test_data")["common_id"]["pw"]


class Test(unittest.TestCase):
    def setUp(self):
        App_setUp(self)
        判断是否需要登录(name, pw)
        关闭告警弹窗()
        close_hub_pairing()

    def tearDown(self):
        sleep(5)
        App_tearDown(self)

    def test_jump_access(self):
        jump_to_access()
        sleep(1)
        断言("access_page", "addCode按钮")

    def test_jump_activity(self):
        jump_to_activity()


if __name__ == '__main__':
    unittest.main()
