from _pyrepl import pager

import pytest
from playwright.sync_api import Page
# (scope="session")
@pytest.fixture
def loging(page):
    page.goto("http://192.168.90.239:60083/#/login")
    page.get_by_role("textbox", name="* 账号").click()
    page.get_by_role("textbox", name="* 账号").fill("huchunchao")
    page.get_by_role("textbox", name="* 密码").click()
    page.get_by_role("textbox", name="* 密码").fill("123456")
    page.get_by_role("button", name="登录").click()
    page.wait_for_url("**/flightTracking/homePage",timeout=50000)
    yield page
    print("登录成功")

    # 录制
    # playwright codegen http: //

    # 有界面运行（推荐，能看到操作过程）
    # pytest
    # test_adsb_config.py - -headed
    #
    # # 无头运行（后台跑，快）
    # pytest
    # test_adsb_config.py
    #
    # # 生成HTML报告
    # pytest
    # test_adsb_config.py - -headed - -html = report.html
