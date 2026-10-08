import pytest

def test_tc03_correct_user_wrong_pass(login_page):
    """
    TC03: Kiểm tra trường hợp đúng tên, sai mật khẩu
    Các bước:
    1. Mở trang https://vanphongdientu.utc.edu.vn/
    2. Click vào ô username và nhập 'huongnt'
    3. Click vào ô password và nhập 'utc@235'
    4. Click vào nút Đăng nhập
    Kỳ vọng:
    Hiển thị thông báo: 'Tài khoản không đúng'
    """
    login_page.login(username="huongnt", password="utc@235")
    
    error_message = login_page.get_error_message()
    assert "không đúng" in error_message.lower(), (
        f"Kỳ vọng thông báo chứa 'không đúng', thực tế nhận: '{error_message}'"
    )
