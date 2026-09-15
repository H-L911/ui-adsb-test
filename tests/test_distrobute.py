import re
from asyncio import timeout

from playwright.sync_api import Playwright, sync_playwright, expect

def test_distrobute(loging):
    page = loging
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
    page.goto("http://192.168.90.239:60083/#/adsb/distribute")
    page.get_by_role("link", name="分发配置").click()
    page.get_by_role("button", name="新增").click()
    page.get_by_role("textbox", name="* 配置名称").click()
    page.get_by_role("textbox", name="* 配置名称").press("CapsLock")
    page.get_by_role("textbox", name="* 配置名称").fill("UI")
    page.get_by_role("textbox", name="* 配置名称").press("CapsLock")
    page.get_by_role("textbox", name="* 配置名称").fill("UI测试2")
    # page.get_by_role("textbox",name="* 推送方式").click()
    page.locator("//div[@class='el-form-item is-required asterisk-left el-form-item--label-right']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").click()
    # page.locator(".el-select__wrapper.is-hovering > .el-select__selection > .el-select__selected-item.el-select__placeholder").click()
    page.get_by_role("option", name="udp").click()
    page.get_by_role("textbox", name="* UDP端口").click()
    page.get_by_role("textbox", name="* UDP端口").fill("5")
    page.get_by_role("textbox", name="* UDP路径").click()
    page.get_by_role("textbox", name="* UDP路径").fill("/data")
    page.get_by_role("textbox", name="* 接收地址").click()
    page.get_by_role("textbox", name="* 接收地址").fill("192.168.3.1")
    page.get_by_role("button", name="确认").click()
    page.wait_for_timeout(2000)#做一个等待要不然页面没有那么快反馈出新增成功
    assert page.get_by_text("新增成功").is_visible()

    # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
