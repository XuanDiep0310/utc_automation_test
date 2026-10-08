import allure
import pytest

@allure.epic("An toàn thông tin (Security)")
@allure.feature("Bảo mật Giao thức & Mạng")
@allure.story("TC15 - Kiểm tra mã hóa dữ liệu HTTPS & SSL")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.security
def test_tc15_https_security(driver):
    """
    TC15: Security Testing - Kiểm tra giao thức bảo mật HTTPS & SSL
    Mục tiêu: Đảm bảo luồng truyền tải thông tin đăng nhập được mã hóa an toàn qua HTTPS,
    ngăn chặn tấn công nghe lén đường truyền mạng (Man-In-The-Middle / Packet Sniffing).
    Các bước:
    1. Truy cập vào trang web https://vanphongdientu.utc.edu.vn/
    2. Kiểm tra URL hiện tại của trình duyệt
    Kỳ vọng:
    - URL bắt đầu bằng giao thức 'https://'
    """
    driver.get("https://vanphongdientu.utc.edu.vn/Login")
    current_url = driver.current_url
    
    assert current_url.startswith("https://"), (
        f"LỖI BẢO MẬT: Kết nối không sử dụng giao thức HTTPS bảo mật! URL hiện tại: {current_url}"
    )
