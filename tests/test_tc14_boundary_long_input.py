import pytest

@pytest.mark.security
def test_tc14_boundary_long_input(login_page, driver):
    """
    TC14: Boundary & Security Testing - Kiểm tra nhập chuỗi ký tự cực dài (5000 ký tự)
    Mục tiêu: Đảm bảo server và client xử lý tốt chuỗi dữ liệu lớn,
    không bị sập bộ đệm (buffer overflow/crash) hoặc làm cạn kiệt tài nguyên xử lý (ReDoS / Resource Exhaustion).
    Các bước:
    1. Tạo chuỗi ký tự gồm 5000 ký tự 'A'
    2. Nhập chuỗi vào ô Username
    3. Nhập mật khẩu: '123'
    4. Click Đăng nhập
    Kỳ vọng:
    - Ứng dụng xử lý ổn định, không treo trình duyệt hoặc crash máy chủ
    - Trả về thông báo lỗi hợp lệ
    """
    long_string = "A" * 5000
    login_page.login(username=long_string, password="123")
    
    error_message = login_page.get_error_message()
    page_source = driver.page_source.lower()
    
    assert "internal server error" not in page_source
    assert len(error_message) > 0, "Kỳ vọng nhận thông báo lỗi hợp lệ khi nhập chuỗi ký tự dài bất thường"
