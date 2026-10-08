import pytest

def test_tc01_empty_username(login_page):
    """
    TC01: Kiểm tra để trống tên đăng nhập
    Các bước:
    1. Mở trang https://vanphongdientu.utc.edu.vn/
    2. Click vào ô username và để trống
    3. Click vào ô password và nhập '1256'
    4. Click vào nút Đăng nhập
    Kỳ vọng:
    Hiển thị thông báo: 'Bạn chưa nhập tên đăng nhập'
    """
    login_page.login(username="", password="1256")
    
    error_message = login_page.get_error_message()
    assert "Bạn chưa nhập tên đăng nhập" in error_message, (
        f"Kỳ vọng thông báo 'Bạn chưa nhập tên đăng nhập', thực tế nhận: '{error_message}'"
    )
