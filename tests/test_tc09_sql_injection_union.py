import pytest

@pytest.mark.security
def test_tc09_sql_injection_union(login_page, driver):
    """
    TC09: Security Testing - Union-based SQL Injection
    Mục tiêu: Đảm bảo kẻ tấn công không thể dùng kỹ thuật UNION SELECT để trích xuất dữ liệu schema.
    Các bước:
    1. Nhập payload UNION SELECT vào ô Username: ' UNION SELECT 1, 'admin', 'hash' --
    2. Nhập mật khẩu: '123'
    3. Click nút Đăng nhập
    Kỳ vọng:
    - Yêu cầu bị từ chối
    - Trang web không hiển thị lỗi 500 hoặc rò rỉ cấu trúc bảng cơ sở dữ liệu
    """
    payload = "' UNION SELECT 1, 'admin', 'hash' --"
    login_page.login(username=payload, password="123")
    
    error_message = login_page.get_error_message()
    page_source = driver.page_source.lower()
    
    assert "internal server error" not in page_source
    assert "union select" not in page_source or "<input" in page_source
    assert "không đúng" in error_message.lower() or "error" in error_message.lower()
