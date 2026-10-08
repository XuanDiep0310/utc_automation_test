import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
import sys
import os

# Đảm bảo import được thư mục gốc của project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Chạy test hiển thị giao diện trình duyệt (mặc định headless)"
    )

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()
    
    # Kiểm tra cờ chạy headed/headless
    if not request.config.getoption("--headed"):
        chrome_options.add_argument("--headless=new")
        
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Khởi tạo driver tự động với webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    
    yield driver
    
    # Tự động chụp màn hình đính kèm vào Allure Report nếu test thất bại
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            pass
            
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook kiểm tra trạng thái kết quả của test case
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

@pytest.fixture(scope="function")
def dashboard_page(driver):
    return DashboardPage(driver)
