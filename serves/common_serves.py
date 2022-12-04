# coding =utf-8
from arize_auto_test.serves.common_Method import *
from arize_auto_test.serves.login_serves import *


def 判断是否需要登录(name, pw):  # 打开app后判断是否需要登录
    if run("login_page", "welcome文案", "exists"):
        登录(name, pw)
    else:
        pass


def 关闭告警弹窗():
    run("dashboard_page", "关闭告警弹窗按钮", "click_if")
