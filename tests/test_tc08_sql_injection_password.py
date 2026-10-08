import pytest

@pytest.mark.security
def test_tc08_sql_injection_password(login_page, driver):
    """
    TC08: Security Testing - SQL Injection Bypass trên trường Password
    Mục tiêu: Đảm bảo trường Password không bị khai thác để sửa đổi logic câu lệnh SELECT SQL.
    Các bước:
    1. Nhập username: 'admin'
    2. Nhập payload SQL injection vào ô Password: ' OR '1'='1
    3. Click nút Đăng nhập
    Kỳ vọng:
    - Không bị bypass đăng nhập trái phép
    - Hiển thị thông báo 'Tài khoản không đúng'
    - Không hiển thị exception stack trace
    """
    payload = "' OR '1'='1"
    login_page.login(username="admin", password=payload)
    
    error_message = login_page.get_error_message()
    page_source = driver.page_source.lower()
    
    assert "syntax error" not in page_source, "Cảnh báo bảo mật: Phát hiện rò rỉ lỗi SQL trong trang!"
    assert "không đúng" in error_message.lower() or "error" in error_message.lower(), (
        f"Kỳ vọng hệ thống từ chối xác thực mật khẩu SQL injection, thực tế: '{error_message}'"
    )
