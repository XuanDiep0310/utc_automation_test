import pytest

def test_tc04_wrong_user_correct_pass(login_page):
    """
    TC04: Kiểm tra trường hợp sai tên, đúng mật khẩu
    Các bước:
    1. Mở trang https://vanphongdientu.utc.edu.vn/
    2. Click vào ô username và nhập 'huongthunguyen'
    3. Click vào ô password và nhập '123456@utc'
    4. Click vào nút Đăng nhập
    Kỳ vọng:
    Hiển thị thông báo: 'Tài khoản không đúng'
    """
    login_page.login(username="huongthunguyen", password="123456@utc")
    
    error_message = login_page.get_error_message()
    assert "không đúng" in error_message.lower(), (
        f"Kỳ vọng thông báo chứa 'không đúng', thực tế nhận: '{error_message}'"
    )
