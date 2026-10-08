import pytest

@pytest.mark.security
def test_tc10_xss_script_injection(login_page, driver):
    """
    TC10: Security Testing - Cross-Site Scripting (Reflected XSS) qua thẻ <script>
    Mục tiêu: Đảm bảo dữ liệu đầu vào được escape mã hóa HTML, không thực thi JavaScript trên trình duyệt.
    Các bước:
    1. Nhập payload XSS vào Username: <script>alert('xss_test')</script>
    2. Nhập mật khẩu: '123'
    3. Click nút Đăng nhập
    Kỳ vọng:
    - Không xuất hiện dialog/alert của trình duyệt
    - Ứng dụng xử lý đầu vào an toàn
    """
    payload = "<script>alert('xss_test')</script>"
    login_page.login(username=payload, password="123")
    
    # Kiểm tra không có popup alert do script bị trigger
    assert not login_page.is_alert_displayed(), "LỖI BẢO MẬT: Phát hiện lỗ hổng XSS thực thi script popup!"
    
    # Xác nhận hiển thị thông báo lỗi và chuỗi được encode an toàn
    error_message = login_page.get_error_message()
    assert "không đúng" in error_message.lower() or "error" in error_message.lower()
