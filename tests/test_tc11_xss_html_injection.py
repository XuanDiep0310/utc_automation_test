import pytest

@pytest.mark.security
def test_tc11_xss_html_injection(login_page, driver):
    """
    TC11: Security Testing - HTML Event-based Injection
    Mục tiêu: Đảm bảo các thuộc tính event handler như onerror trong thẻ HTML không bị chèn vào DOM.
    Các bước:
    1. Nhập payload vào Username: \"><img src=x onerror=alert('xss')>
    2. Nhập mật khẩu: '123'
    3. Click nút Đăng nhập
    Kỳ vọng:
    - Không kích hoạt alert box
    - Hệ thống xử lý chuỗi an toàn
    """
    payload = '\"><img src=x onerror=alert("xss")>'
    login_page.login(username=payload, password="123")
    
    assert not login_page.is_alert_displayed(), "LỖI BẢO MẬT: Phát hiện thẻ HTML injection kích hoạt JavaScript event!"
    error_message = login_page.get_error_message()
    assert len(error_message) > 0
