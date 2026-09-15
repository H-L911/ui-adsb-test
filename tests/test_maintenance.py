
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_maintenance(loging):
    page = loging
    #新增变量测试数据为后面编辑定位到数据提供便利
    goods_name = 'ui测试数据' + str(int(time.time()))#str时间戳形式
    print(f"本次生成的商品名：{goods_name}")

    page.goto("http://192.168.90.239:60083/#/adsb/maintenance")
    page.get_by_text("产品管理").click()
    page.get_by_role("link", name="产品维护").click()
    #新增
    page.get_by_text("点击新增产品").click()
    # page.locator("div").filter(has_text=re.compile(r"^请选择产品类型$")).nth(4).click()
    page.locator("//form[@class='el-form el-form--default el-form--label-right product-form']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    page.get_by_role("option", name="测试类型(原始数据)", exact=True).click()
    page.get_by_text("请选择计费规则").click()
    page.get_by_text("现场测试计费规则").click()
    page.get_by_text("请选择产品编号").click()
    page.get_by_role("option", name="DF17", exact=True).click()
    page.get_by_role("textbox", name="* 产品名称").click()
    page.get_by_role("textbox", name="* 产品名称").fill(goods_name)
    page.get_by_role("textbox", name="折扣").click()
    page.get_by_role("textbox", name="折扣").fill("5")
    page.get_by_text("请选择服务周期").click()
    # page.locator("div").filter(has_text=re.compile(r"^请选择服务周期$")).nth(4).click()
    page.get_by_role("option", name="日").click()
    page.get_by_role("textbox", name="* 服务时间").click()
    page.get_by_role("textbox", name="* 服务时间").fill("31")
    page.get_by_role("textbox", name="* 产品描述").click()
    page.get_by_role("textbox", name="* 产品描述").fill("测试一下")
    page.locator("#w-e-textarea-1").click()
    page.locator("#w-e-textarea-1").fill("测试一下")
    #上传附件
    # 直接给 input 元素设置文件路径
    # page.get_by_label("上传附件").set_input_files("E:/新建文件夹/UI测试/1.jpg")
    # 也可以按照xpath写法
    # page.locator("input[type='file']").set_input_files("E:/新建文件夹/UI测试/1.jpg")
    #用xpath绝对路径定位必须定位到这个上传文件的input标签位置
    page.locator("//div[@class='el-form-item asterisk-left el-form-item--label-right']/div[2]/div[1]/div[1]/div[1]/input[1]").set_input_files("E:/新建文件夹/UI测试/1.jpg")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="确认").click()
    page.wait_for_timeout(1000)  # 做一个等待要不然页面没有那么快反馈出新增成功
    #断言
    assert page.get_by_text("新增成功").is_visible()
    # card = page.locator("div.product-card").filter(has_text=goods_name)
    #校验商品出现在列表
    page.locator("div.product-card").filter(has_text=goods_name).wait_for(state="visible", timeout=5000)
    print("商品已出现在列表里")

    # page.locator("div.product-card").filter(has_text=goods_name).get_by_role("button", name="编辑").click()
    #编辑
    page.locator("div.product-card").filter(has_text=goods_name).locator("//div[@class='footer']/div[1]/a[1]/span[1]").click()
    print("已点击编辑按钮")
    page.get_by_role("textbox", name="折扣").click()
    page.get_by_role("textbox", name="折扣").fill("10")
    page.get_by_role("button", name="确认").click()
    page.wait_for_timeout(1000)  # 做一个等待要不然页面没有那么快反馈出新增成功
    # 断言
    assert page.get_by_text("保存成功").is_visible()
    #删除
    page.locator("div.product-card").filter(has_text=goods_name).locator("//div[@class='footer']/div[1]/a[2]/span[1]").click()
    # page.locator("div.product-card").filter(has_text=goods_name).locator("//div[@class='el-popper is-light el-tooltip el-popover']/div[1]/div[2]/button[2]").click()
    # page.locator("div.product-card").filter(has_text=goods_name).locator(".el-popconfirm").get_by_role("button", name="确定").click(force=True)#用这段代码定位不到前端删除的确定没在卡片里他俩根目录压根就没在一个div里你后面写.locator没用。


    page.locator(".el-popconfirm:visible").get_by_role("button", name="确定").click()
    print("已点击删除按钮")

    page.wait_for_timeout(1000)  # 做一个等待要不然页面没有那么快反馈出新增成功
    # 断言
    assert page.get_by_text("删除成功").is_visible()





