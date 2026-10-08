import allure
import pytest
import requests

@allure.epic("An toàn thông tin (Security)")
@allure.feature("Tính sẵn sàng & Phòng thủ DoS (Resilience)")
@allure.story("TC12 - Khả năng chịu tải và phòng thủ request dồn dập (Anti-DoS / Rate Limit)")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.security
def test_tc12_rate_limit_dos_resilience(login_page):
    """
    TC12: Security Testing - Kiểm tra khả năng xử lý request dồn dập (Anti-DoS / Rate Limit Resilience)
    Mục tiêu: Đảm bảo khi nhận nhiều yêu cầu xác thực liên tiếp trong khoảng thời gian ngắn,
    hệ thống không bị sập dịch vụ (Internal Server Error 500) và duy trì tính khả dụng (Availability).
    Các bước:
    1. Gửi mô phỏng 5 yêu cầu đăng nhập liên tiếp với thông tin ngẫu nhiên
    2. Kiểm tra mã trạng thái phản hồi HTTP của từng yêu cầu
    3. Kiểm tra trang đăng nhập vẫn hoạt động bình thường trên trình duyệt
    Kỳ vọng:
    - Server không trả về mã lỗi 500 hoặc bị crash
    - Mã trạng thái phản hồi hợp lệ (200 OK, 302 Redirect hoặc 429 Too Many Requests)
    """
    url = "https://vanphongdientu.utc.edu.vn/Login"
    session = requests.Session()
    
    status_codes = []
    # Gửi 5 yêu cầu liên tiếp một cách có kiểm soát
    for i in range(5):
        try:
            resp = session.post(
                url,
                data={"username": f"test_rate_user_{i}", "userpwd": "wrong_password"},
                verify=False,
                timeout=10
            )
            status_codes.append(resp.status_code)
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Lỗi kết nối khi gửi yêu cầu kiểm tra: {e}")
            
    # Kiểm tra server không bị sập (không có mã 500 hoặc 503 sập hoàn toàn)
    for code in status_codes:
        assert code != 500, "CẢNH BÁO: Phát hiện mã lỗi 500 Internal Server Error khi nhận yêu cầu dồn dập!"
        assert code in [200, 302, 429, 403], f"Mã trạng thái phản hồi không mong muốn: {code}"
        
    # Xác nhận trang đăng nhập trên trình duyệt vẫn tải tốt
    login_page.open()
    login_page.wait_for_page_ready()
