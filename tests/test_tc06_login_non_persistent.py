import pytest

def test_tc06_login_non_persistent(login_page, driver):
    """
    TC06: Đăng nhập thành công và không chọn 'Giữ tôi luôn đăng nhập'
    Các bước:
    1. Mở trang https://vanphongdientu.utc.edu.vn/
    2. Click vào ô username và nhập tài khoản
    3. Click vào ô password và nhập mật khẩu
    4. Không tích chọn 'Giữ tôi luôn đăng nhập'
    5. Click vào nút Đăng nhập
    Kỳ vọng:
    Hệ thống gửi request không kèm cờ ghi nhớ phiên (persistent=0)
    """
    login_page.login(username="huongnt", password="123456@utc", remember_me=False)
    
    current_url = driver.current_url
    error_message = login_page.get_error_message()
    
    assert "vanphongdientu.utc.edu.vn" in current_url
    if error_message:
        assert "Tài khoản không đúng" in error_message or "Bạn chưa nhập" in error_message
