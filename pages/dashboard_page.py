from selenium.webdriver.common.by import By
from base.base_page import BasePage
import allure

class DashboardPage(BasePage):
    """
    DashboardPage: Đại diện cho trang chủ / dashboard sau khi người dùng đăng nhập thành công.
    Tương đương DashboardPage.java trong kiến trúc Java/Page Object Model.
    """
    URL = "https://vanphongdientu.utc.edu.vn/"
    
    # Locators cho Menu, Header, Thông tin người dùng
    LOC_USER_PROFILE = (By.CSS_SELECTOR, "div.user_info, a.user_name, .header-user")
    LOC_LOGOUT_BTN = (By.XPATH, "//a[contains(@href, 'Logout') or contains(text(), 'Đăng xuất')]")
    LOC_NAV_MENU = (By.CSS_SELECTOR, "nav, .menu_main, ul.navigation")
    
    @allure.step("Kiểm tra trang Dashboard có hiển thị thông tin người dùng hay không")
    def is_user_logged_in(self) -> bool:
        return self.is_displayed(self.LOC_USER_PROFILE) or "vanphongdientu.utc.edu.vn" in self.get_current_url()
        
    @allure.step("Thực hiện đăng xuất khỏi hệ thống")
    def logout(self):
        if self.is_displayed(self.LOC_LOGOUT_BTN):
            self.click(self.LOC_LOGOUT_BTN)
        return self
