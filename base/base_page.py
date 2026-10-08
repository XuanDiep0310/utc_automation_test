from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class BasePage:
    """
    BasePage: Lớp cơ sở chứa toàn bộ các thao tác dùng chung cho các trang (Page Objects).
    Tương đương BasePage.java trong kiến trúc Java/Selenium.
    """
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    @allure.step("Mở URL: {url}")
    def open_url(self, url: str):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Click vào phần tử: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    @allure.step("Nhập văn bản vào: {locator}")
    def send_keys(self, locator, text: str, clear: bool = True):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if clear:
            element.clear()
        if text:
            element.send_keys(text)
        return self

    def get_text(self, locator) -> str:
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            return ""

    def is_displayed(self, locator) -> bool:
        try:
            return self.driver.find_element(*locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def is_alert_present(self, timeout=2) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def get_alert_text(self) -> str:
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except Exception:
            return ""

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_source(self) -> str:
        return self.driver.page_source
