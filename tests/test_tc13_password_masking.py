import pytest

@pytest.mark.security
def test_tc13_password_masking(login_page):
    """
    TC13: Security Testing - Kiểm tra che giấu ký tự mật khẩu (Password Masking)
    Mục tiêu: Đảm bảo trường nhập mật khẩu được cấu hình type='password' trong HTML DOM,
    ngăn ngừa lộ mật khẩu trước các nguy cơ nhìn trộm màn hình (shoulder surfing).
    Các bước:
    1. Mở trang đăng nhập
    2. Kiểm tra thuộc tính type của ô mật khẩu
    3. Nhập chuỗi mật khẩu thử nghiệm
    Kỳ vọng:
    - Thuộc tính type='password'
    - Ký tự được hiển thị dưới dạng dấu chấm hoặc ký tự ẩn
    """
    assert login_page.is_password_masked(), (
        "LỖI BẢO MẬT: Trường mật khẩu không có thuộc tính type='password', mật khẩu bị lộ dạng clear text!"
    )
