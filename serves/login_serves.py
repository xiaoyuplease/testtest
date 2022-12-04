from arize_auto_test.serves.common_Method import *
import random


def 登录(name, pw):#登录流程
    run("login_page", "Email按钮", "input", name)
    run("login_page", "Password按钮", "input", pw)
    A = random.choice([1, 2])
    if A == 1:
        run("login_page", "显示密码按钮", "click")
    else:
        pass
    run("login_page", "登录按钮", "click")

def 从登录页面跳转到dashboard():#从登录页面跳转到注册
    run("login_page", "登录按钮", "click")

def 从登录页面跳转到忘记密码():#从登录页面跳转到忘记密码
    run("login_page", "忘记密码按钮", "click")


