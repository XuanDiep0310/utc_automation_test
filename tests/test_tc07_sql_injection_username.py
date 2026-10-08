import pytest

@pytest.mark.security
def test_tc07_sql_injection_username(login_page, driver):
    """
    TC07: Security Testing - SQL Injection Bypass trên trường Username
    Mục tiêu: Đảm bảo hệ thống sử dụng Prepared Statements/Parameterized Queries,
    ngăn chặn kẻ tấn công vượt qua xác thực bằng SQL injection payload.
    Các bước:
    1. Nhập payload SQL injection vào ô Username: ' OR '1'='1 --
    2. Nhập password bất kỳ: password123
    3. Click nút Đăng nhập
    Kỳ vọng:
    - Không bị bypass đăng nhập
    - Trả về thông báo lỗi chuẩn 'Tài khoản không đúng'
    - Không để lộ lỗi cú pháp SQL (SQL syntax error, ODBC/OLEDB exception)
    """
    payload = "' OR '1'='1 --"
    login_page.login(username=payload, password="password123")
    
    error_message = login_page.get_error_message()
    page_source = driver.page_source.lower()
    
    # Xác nhận hệ thống không bị crash hoặc rò rỉ database error
    assert "syntax error" not in page_source, "Cảnh báo bảo mật: Phát hiện rò rỉ lỗi cú pháp SQL!"
    assert "sqlserver" not in page_source and "mysql" not in page_source, "Cảnh báo bảo mật: Rò rỉ thông tin CSDL!"
    
    # Xác nhận hệ thống từ chối đăng nhập với thông báo lỗi bảo mật chuẩn
    assert "không đúng" in error_message.lower() or "error" in error_message.lower(), (
        f"Kỳ vọng hệ thống từ chối xác thực SQL injection, thực tế: '{error_message}'"
    )
