# UTC E-Office (vanphongdientu.utc.edu.vn) - Automation Testing Framework

Dự án kiểm thử tự động (Automation Testing) cho phân hệ Đăng nhập của hệ thống Văn phòng điện tử Trường Đại học Giao thông vận tải (UTC) tại địa chỉ: `https://vanphongdientu.utc.edu.vn/`.

Dự án được xây dựng theo mô hình **Page Object Model (POM)** kết hợp với **Pytest** và **Selenium WebDriver**, bao gồm đầy đủ các kịch bản kiểm thử chức năng (theo Bảng quyết định - Decision Table) và các kịch bản kiểm thử bảo mật nâng cao (SQL Injection, XSS, DoS / Rate Limiting resilience, Password Masking, Boundary Value, HTTPS).

---

## 📁 Cấu trúc dự án

```text
utc_automation_test/
│── testcases/
│   └── testcases_vanphongdientu.xlsx       # File Excel chứa Bảng quyết định và danh sách chi tiết Test Cases
│── pages/
│   ├── __init__.py
│   └── login_page.py                       # Page Object Model quản lý tương tác và định vị phần tử trang đăng nhập
│── tests/
│   ├── __init__.py
│   ├── conftest.py                         # Cấu hình Pytest fixture (Chrome WebDriver headless/headed, SSL options)
│   ├── test_tc01_empty_username.py         # TC01: Kiểm tra để trống tên đăng nhập
│   ├── test_tc02_empty_password.py         # TC02: Kiểm tra để trống mật khẩu
│   ├── test_tc03_correct_user_wrong_pass.py# TC03: Kiểm tra đúng tên sai mật khẩu
│   ├── test_tc04_wrong_user_correct_pass.py# TC04: Kiểm tra sai tên đúng mật khẩu
│   ├── test_tc05_login_persistent.py       # TC05: Đăng nhập thành công và chọn 'Giữ tôi luôn đăng nhập'
│   ├── test_tc06_login_non_persistent.py   # TC06: Đăng nhập thành công và không chọn 'Giữ tôi luôn đăng nhập'
│   ├── test_tc07_sql_injection_username.py # TC07: Security - SQL Injection bypass trên trường Username
│   ├── test_tc08_sql_injection_password.py # TC08: Security - SQL Injection bypass trên trường Password
│   ├── test_tc09_sql_injection_union.py    # TC09: Security - Union-based SQL Injection khai thác cấu trúc CSDL
│   ├── test_tc10_xss_script_injection.py   # TC10: Security - Cross-Site Scripting (XSS) qua thẻ <script>
│   ├── test_tc11_xss_html_injection.py     # TC11: Security - HTML Event Injection (onerror tag)
│   ├── test_tc12_rate_limit_dos_resilience.py # TC12: Security - Kiểm tra khả năng chịu tải dồn dập (Anti-DoS / Brute-force)
│   ├── test_tc13_password_masking.py       # TC13: Security - Kiểm tra mã hóa hiển thị trường mật khẩu (type='password')
│   ├── test_tc14_boundary_long_input.py    # TC14: Security / Boundary - Kiểm tra nhập chuỗi ký tự cực dài (5000 chars)
│   └── test_tc15_https_security.py         # TC15: Security - Kiểm tra kết nối an toàn giao thức HTTPS & SSL
│── generate_excel.py                       # Script Python tạo và định dạng file Excel test cases
│── requirements.txt                        # Danh sách thư viện phụ thuộc
│── README.md                               # Tài liệu hướng dẫn dự án
└── .gitignore
```

---

## 📊 Ma trận kiểm thử & Bảng quyết định (Decision Table)

File Excel `testcases/testcases_vanphongdientu.xlsx` bao gồm 2 Sheets:

1. **Bảng quyết định**:
   - Quy tắc R1: Tên đăng nhập = False -> Hiển thị lỗi / Sai tài khoản.
   - Quy tắc R2: Tên đăng nhập = True, Mật khẩu = False -> Hiển thị lỗi / Sai tài khoản.
   - Quy tắc R3: Tên đăng nhập = True, Mật khẩu = True, Giữ đăng nhập = False -> Vào trang chủ. Tắt trình duyệt và mở lại thì cần đăng nhập lại.
   - Quy tắc R4: Tên đăng nhập = True, Mật khẩu = True, Giữ đăng nhập = True -> Vào trang chủ. Tắt trình duyệt và mở lại thì không cần đăng nhập lại.

2. **Danh sách Test Case (15 Test Cases)**:
   - **Chức năng (TC01 - TC06)**: Kiểm tra validation bỏ trống, sai tài khoản, ghi nhớ phiên đăng nhập.
   - **Bảo mật SQL Injection (TC07 - TC09)**: Kiểm thử phòng vệ injection, parameterized query, ngăn ngừa rò rỉ database error.
   - **Bảo mật XSS (TC10 - TC11)**: Kiểm thử lọc mã độc script và html tag injection.
   - **Bảo mật DoS / Rate Limit (TC12)**: Kiểm thử độ sẵn sàng của hệ thống khi gửi liên tiếp các yêu cầu (Resilience test).
   - **Bảo mật Giao diện & Hạ tầng (TC13 - TC15)**: Password masking, chống buffer overflow, giao thức HTTPS.

---

## 🚀 Cài đặt & Hướng dẫn thực thi

### 1. Cài đặt thư viện phụ thuộc
```bash
pip install -r requirements.txt
```

### 2. Tạo lại file Excel testcase (nếu cần cập nhật)
```bash
python generate_excel.py
```

### 3. Thực thi kiểm thử tự động với Pytest

- **Chạy toàn bộ test suite (mặc định chạy ngầm - Headless mode):**
  ```bash
  pytest -v
  ```

- **Chạy kèm giao diện trình duyệt trực quan (Headed mode):**
  ```bash
  pytest -v --headed
  ```

- **Chạy riêng một test case cụ thể:**
  ```bash
  pytest tests/test_tc01_empty_username.py -v
  ```

- **Chạy riêng nhóm kiểm thử bảo mật (Security tests):**
  ```bash
  pytest -k "sql or xss or dos or security or masking" -v
  ```

---

## 📌 Lịch sử Git Commits

Dự án được phân bổ lịch sử commit chi tiết theo đúng yêu cầu:
1. `feat: khoi tao du an kiem thu tu dong van phong dien tu utc gom excel testcase va pom`
2. `test: them khao sat va testcase tc01 kiem tra de trong ten dang nhap`
3. `test: them testcase tc02 kiem tra de trong mat khau`
4. `test: them testcase tc03 kiem tra dung ten sai mat khau`
5. `test: them testcase tc04 kiem tra sai ten dung mat khau`
6. `test: them testcase tc05 kiem tra dang nhap thanh cong co chon giu toi luon dang nhap`
7. `test: them testcase tc06 kiem tra dang nhap thanh cong khong chon giu toi luon dang nhap`
8. `test: them security testcase tc07 sql injection bypass tren truong username`
9. `test: them security testcase tc08 sql injection bypass tren truong password`
10. `test: them security testcase tc09 union sql injection khai thac csdl`
11. `test: them security testcase tc10 xss script tag injection`
12. `test: them security testcase tc11 xss html event onerror injection`
13. `test: them security testcase tc12 kiem tra kha nang chiu tai va chong request don dap anti-dos`
14. `test: them security testcase tc13 kiem tra che giau ky tu mat khau password masking`
15. `test: them security testcase tc14 kiem tra gioi han do dai chuoi cuc lon buffer boundary`
16. `test: them security testcase tc15 kiem tra bao mat ket noi giao thuc https`
