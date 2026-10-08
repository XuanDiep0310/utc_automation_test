from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

class LoginPage:
    URL = "https://vanphongdientu.utc.edu.vn/Login"
    
    # Locators
    LOC_USERNAME = (By.NAME, "username")
    LOC_PASSWORD = (By.NAME, "userpwd")
    LOC_REMEMBER_ME = (By.NAME, "persistent")
    LOC_REMEMBER_ME_LABEL = (By.CSS_SELECTOR, "label.check")
    LOC_SUBMIT_BTN = (By.CSS_SELECTOR, "input.submit_login")
    LOC_ERROR_MSG = (By.CSS_SELECTOR, "div.error")
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        
    def open(self):
        """Mở trang đăng nhập"""
        self.driver.get(self.URL)
        self.wait_for_page_ready()
        return self
        
    def wait_for_page_ready(self):
        """Chờ DOM tải xong và form xuất hiện"""
        self.wait.until(EC.presence_of_element_located(self.LOC_USERNAME))
        
    def enter_username(self, username: str):
        """Nhập tên đăng nhập"""
        field = self.wait.until(EC.element_to_be_clickable(self.LOC_USERNAME))
        field.clear()
        if username:
            field.send_keys(username)
        return self
        
    def enter_password(self, password: str):
        """Nhập mật khẩu"""
        field = self.wait.until(EC.element_to_be_clickable(self.LOC_PASSWORD))
        field.clear()
        if password:
            field.send_keys(password)
        return self
        
    def set_remember_me(self, check: bool = True):
        """Bật / tắt tùy chọn 'Giữ tôi luôn đăng nhập'"""
        checkbox = self.driver.find_element(*self.LOC_REMEMBER_ME)
        is_selected = checkbox.is_selected()
        if (check and not is_selected) or (not check and is_selected):
            try:
                # Do giao diện tùy biến che giấu checkbox native và dùng label.check
                label = self.driver.find_element(*self.LOC_REMEMBER_ME_LABEL)
                label.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", checkbox)
        return self
        
    def click_login(self):
        """Nhấn nút Đăng nhập"""
        btn = self.wait.until(EC.element_to_be_clickable(self.LOC_SUBMIT_BTN))
        btn.click()
        return self
        
    def login(self, username: str = "", password: str = "", remember_me: bool = False):
        """Thực hiện chuỗi hành động đăng nhập đầy đủ"""
        self.enter_username(username)
        self.enter_password(password)
        if remember_me:
            self.set_remember_me(True)
        self.click_login()
        return self
        
    def get_error_message(self) -> str:
        """Lấy nội dung thông báo lỗi hiển thị trên trang"""
        try:
            error_elem = self.wait.until(EC.visibility_of_element_located(self.LOC_ERROR_MSG))
            return error_elem.text.strip()
        except TimeoutException:
            return ""
            
    def is_password_masked(self) -> bool:
        """Kiểm tra trường mật khẩu có che giấu ký tự (type='password') hay không"""
        elem = self.driver.find_element(*self.LOC_PASSWORD)
        return elem.get_attribute("type") == "password"
        
    def is_alert_displayed(self) -> bool:
        """Kiểm tra có popup alert của trình duyệt xuất hiện hay không"""
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_to_present())
            return True
        except TimeoutException:
            return False
            
    def get_alert_text_and_dismiss(self) -> str:
        """Lấy nội dung alert và đóng popup"""
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except Exception:
            return ""
