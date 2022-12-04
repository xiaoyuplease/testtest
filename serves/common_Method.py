import yaml
import uiautomator2 as u2
import os
from time import sleep

basePath = os.path.dirname(os.path.dirname(__file__))
print(basePath)


# 读取page下面的yaml文件
def open_yaml_page(file):
    with open(basePath + "/page/%s" % file + ".yaml", "r", encoding="utf-8") as f:
        f = yaml.load(f, Loader=yaml.FullLoader)
    return f


# 去读data下面的yaml文件
def open_yaml_data(file):
    with open(basePath + "/data/%s" % file + ".yaml", "r", encoding="utf-8") as f:
        f = yaml.load(f, Loader=yaml.FullLoader)
    return f


devices_type = open_yaml_data("configure_data")["devices_type"]

environmental = open_yaml_data("configure_data")["environmental"]

if environmental == "test":
    a_appName = open_yaml_data("configure_data")["a_test_appName"]

else:
    a_appName = open_yaml_data("configure_data")["a_prd_appName"]

if devices_type == "a":
    d = u2.connect("RF8M826HP4H")


    def App_setUp(self):
        self.d = d
        self.d.screen_on()
        self.d.unlock()
        self.d.set_fastinput_ime(True)
        self.d.app_start(a_appName, use_monkey=True)
        self.d.settings["wait_timeout"] = 10
        self.d.settings["operation_delay"] = (.5, 1)
        sleep(2)


    def App_tearDown(self):
        self.d = d
        self.d.app_stop(a_appName)


def find_ele(file, ele):
    data = open_yaml_page(file)
    if environmental == "test":
        if devices_type == "a":
            index = 0
            if data[ele]["a_find_type"] == "text":
                element = d(text=data[ele]["a_element_info"])[index]
            elif data[ele]["a_find_type"] == "id":
                element = d(resourceId=data[ele]["a_element_info"])[index]
            elif data[ele]["a_find_type"] == "xpath":
                element = d.xpath(data[ele]["a_element_info"])
        return element


def run(file: object, ele: object, action: object, content: object = "123") -> object:
    element = find_ele(file, ele)
    if devices_type == "a":
        if action == "click":
            element.click()
        elif action == "input":
            element.click()
            d.send_keys(content, clear=True)
        elif action == "click_if":
            element.click_exists(timeout=5)
        elif action == "exists":
            return element.exists(timeout=5)


def 断言(file, ele):
    sleep(2)
    element = find_ele(file, ele)
    if devices_type == "a":
        A = element.exists(timeout=5)
    return A


def get_text_value(tv):
    text = ""
    if devices_type == "a":
        text = tv.get_text()
    return text
