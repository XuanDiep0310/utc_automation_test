from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.base_page import BasePage
import allure

class LoginPage(BasePage):
    """
    LoginPage: Quản lý toàn bộ giao diện và thao tác trên form đăng nhập.
    Tương đương LoginPage.java trong kiến trúc Java/Page Object Model.
    Kế thừa từ BasePage.
    """
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    
    # Locators
    LOC_USERNAME = (By.NAME, "username")
    LOC_PASSWORD = (By.NAME, "userpwd")
    LOC_REMEMBER_ME = (By.NAME, "persistent")
    LOC_REMEMBER_ME_LABEL = (By.CSS_SELECTOR, "label.check")
    LOC_SUBMIT_BTN = (By.CSS_SELECTOR, "input.submit_login")
    LOC_ERROR_MSG = (By.CSS_SELECTOR, "div.error")
    
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        
    @allure.step("Mở trang Đăng nhập UTC: https://vanphongdientu.utc.edu.vn/Login")
    def open(self):
        """Mở trang đăng nhập"""
        self.open_url(self.URL)
        self.wait_for_page_ready()
        return self
        
    def wait_for_page_ready(self):
        """Chờ DOM tải xong và form xuất hiện"""
        self.wait.until(EC.presence_of_element_located(self.LOC_USERNAME))
        
    @allure.step("Nhập tên đăng nhập: '{username}'")
    def enter_username(self, username: str):
        """Nhập tên đăng nhập"""
        self.send_keys(self.LOC_USERNAME, username)
        return self
        
    @allure.step("Nhập mật khẩu (đã che giấu)")
    def enter_password(self, password: str):
        """Nhập mật khẩu"""
        self.send_keys(self.LOC_PASSWORD, password)
        return self
        
    @allure.step("Thiết lập tùy chọn 'Giữ tôi luôn đăng nhập': {check}")
    def set_remember_me(self, check: bool = True):
        """Bật / tắt tùy chọn 'Giữ tôi luôn đăng nhập'"""
        checkbox = self.driver.find_element(*self.LOC_REMEMBER_ME)
        is_selected = checkbox.is_selected()
        if (check and not is_selected) or (not check and is_selected):
            try:
                # Do giao diện jQuery tùy biến che giấu checkbox native và dùng label.check
                label = self.driver.find_element(*self.LOC_REMEMBER_ME_LABEL)
                label.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", checkbox)
        return self
        
    @allure.step("Nhấn nút Đăng nhập")
    def click_login(self):
        """Nhấn nút Đăng nhập"""
        self.click(self.LOC_SUBMIT_BTN)
        return self
        
    @allure.step("Thực hiện đăng nhập với tài khoản: '{username}'")
    def login(self, username: str = "", password: str = "", remember_me: bool = False):
        """Thực hiện chuỗi hành động đăng nhập đầy đủ"""
        self.enter_username(username)
        self.enter_password(password)
        if remember_me:
            self.set_remember_me(True)
        self.click_login()
        return self
        
    @allure.step("Đọc nội dung thông báo lỗi từ hệ thống")
    def get_error_message(self) -> str:
        """Lấy nội dung thông báo lỗi hiển thị trên trang"""
        return self.get_text(self.LOC_ERROR_MSG)
            
    def is_password_masked(self) -> bool:
        """Kiểm tra trường mật khẩu có che giấu ký tự (type='password') hay không"""
        elem = self.driver.find_element(*self.LOC_PASSWORD)
        return elem.get_attribute("type") == "password"
        
    def is_alert_displayed(self) -> bool:
        """Kiểm tra có popup alert của trình duyệt xuất hiện hay không"""
        return self.is_alert_present(timeout=2)
            
    def get_alert_text_and_dismiss(self) -> str:
        """Lấy nội dung alert và đóng popup"""
        return self.get_alert_text()
