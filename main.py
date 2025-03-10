from playwright.sync_api import sync_playwright

# 使用 Playwright 上下文管理器
with sync_playwright() as p:
    # 启动 Firefox 浏览器
    browser = p.firefox.launch(headless=False)  # headless=False 显示浏览器窗口
    page = browser.new_page()

    # 访问信用中国首页
    page.goto("https://www.creditchina.gov.cn/", wait_until="networkidle")

    # 等待页面加载完成
    page.wait_for_load_state("networkidle")

    # 获取页面标题
    title = page.title()
    print(f"页面标题: {title}")

    # 可选：截图保存
    page.screenshot(path="creditchina_homepage.png")

    # 关闭浏览器
    browser.close()