import pytest

def test_tc02_empty_password(login_page):
    """
    TC02: Kiểm tra để trống mật khẩu
    Các bước:
    1. Mở trang https://vanphongdientu.utc.edu.vn/
    2. Click vào ô username và nhập 'huongnt'
    3. Click vào ô password và để trống
    4. Click vào nút Đăng nhập
    Kỳ vọng:
    Hiển thị thông báo: 'Bạn chưa nhập mật khẩu'
    """
    login_page.login(username="huongnt", password="")
    
    error_message = login_page.get_error_message()
    assert "Bạn chưa nhập mật khẩu" in error_message, (
        f"Kỳ vọng thông báo 'Bạn chưa nhập mật khẩu', thực tế nhận: '{error_message}'"
    )
