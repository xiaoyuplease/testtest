# coding=utf-8
from arize_auto_test.serves.common_Method import *


def jump_to_dashboard():
    run("dashboard_page", "dashboard按钮", "click")


def jump_to_access():
    run("dashboard_page", "Access按钮", "click")


def jump_to_activity():
    run("dashboard_page", "Activity按钮", "click")


def show_pulldown_list():
    run("dashboard_page", "下拉房间列表按钮", "click")


def jump_to_profile():
    run("dashboard_page", "左上角菜单按钮", "click")


def jump_to_devicesetting():
    run("dashboard_page", "设备设置按钮", "click")


def close_room_list():
    run("dashboard_page", "关闭房间列表按钮", "click")


def hub_pairing():
    run("dashboard_page", "网关配网按钮", "click")

# def back_to_dashboard():
#     run("")


def close_hub_pairing():
    if run("dashboard_page", "网关配网按钮", "exists"):
        hub_pairing()
        # back_to_dashboard()
    else:
        pass

