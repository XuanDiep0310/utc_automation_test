# UTC E-Office (vanphongdientu.utc.edu.vn) - Automation Testing Framework

Dự án kiểm thử tự động (Automation Testing) cho phân hệ Đăng nhập của hệ thống Văn phòng điện tử Trường Đại học Giao thông vận tải (UTC) tại địa chỉ: `https://vanphongdientu.utc.edu.vn/`.

Dự án được xây dựng theo chuẩn công nghiệp **Page Object Model (POM)** kết hợp với **Pytest**, **Selenium WebDriver**, và hệ thống báo cáo trực quan **Allure Report & Pytest-HTML**, tích hợp đường ống **CI/CD GitHub Actions**.

---

## 📁 Cấu trúc dự án (Architecture)

Cấu trúc tương đồng với kiến trúc chuẩn trong các dự án E2E Testing chuyên nghiệp:

```text
utc_automation_test/
│── base/                                   # CAC LOP CO SO DUNG CHUNG
│   ├── __init__.py
│   ├── base_page.py                        # BasePage: thao tac chung (wait, click, type, alert, screenshot)
│   └── base_test.py                        # BaseTest: khoi tao WebDriver, timeout, fixture ke thua
│── pages/                                  # CAC PAGE OBJECTS (POM)
│   ├── __init__.py
│   ├── login_page.py                       # LoginPage: Form dang nhap, ke thua tu BasePage
│   └── dashboard_page.py                   # DashboardPage: Menu, Header, thong tin user sau dang nhap
│── tests/                                  # CAC TEST SCRIPTS (PYTEST & ALLURE)
│   ├── __init__.py
│   ├── conftest.py                         # Fixtures WebDriver, Allure screenshot on failure
│   ├── test_tc01_empty_username.py         # TC01: Kiem tra de trong ten dang nhap
│   ├── test_tc02_empty_password.py         # TC02: Kiem tra de trong mat khau
│   ├── test_tc03_correct_user_wrong_pass.py# TC03: Dung ten sai mat khau
│   ├── test_tc04_wrong_user_correct_pass.py# TC04: Sai ten dung mat khau
│   ├── test_tc05_login_persistent.py       # TC05: Dang nhap co chon 'Giu toi luon dang nhap'
│   ├── test_tc06_login_non_persistent.py   # TC06: Dang nhap khong chon 'Giu toi luon dang nhap'
│   ├── test_tc07_sql_injection_username.py # TC07: Security - SQL Injection bypass tren Username
│   ├── test_tc08_sql_injection_password.py # TC08: Security - SQL Injection bypass tren Password
│   ├── test_tc09_sql_injection_union.py    # TC09: Security - Union SQL Injection khai thac CSDL
│   ├── test_tc10_xss_script_injection.py   # TC10: Security - Cross-Site Scripting qua the <script>
│   ├── test_tc11_xss_html_injection.py     # TC11: Security - HTML Event Injection qua the onerror
│   ├── test_tc12_rate_limit_dos_resilience.py # TC12: Security - Kiem tra chiu tai don dap (Anti-DoS)
│   ├── test_tc13_password_masking.py       # TC13: Security - Che giau ky tu mat khau (type='password')
│   ├── test_tc14_boundary_long_input.py    # TC14: Security - Kiem tra chuoi cuc dai 5000 ky tu
│   └── test_tc15_https_security.py         # TC15: Security - Kiem tra giao thuc HTTPS & SSL
│── .github/
│   └── workflows/
│       └── ci.yml                          # Pipeline CI/CD GitHub Actions tu dong chay & tao Allure Report
│── testcases/
│   └── testcases_vanphongdientu.xlsx       # File Excel gom Bang quyet dinh & 15 Test Cases chi tiet
│── reports/                                # Thu muc chua bao cao sau khi thuc thi
│   ├── report.html                         # Bao cao HTML truc quan (pytest-html)
│   └── allure-results/                     # Du lieu sinh bao cao Allure Report
│── generate_excel.py                       # Script sinh file Excel testcase tu dong
│── pytest.ini                              # Cau hinh pytest, markers, alluredir, html report
│── requirements.txt                        # Danh sach thu vien phu thuoc
└── README.md
```

---

## 📊 Báo cáo Kiểm thử: Allure Report & HTML Report

Dự án hỗ trợ 2 dạng báo cáo chuyên nghiệp tương tự bên Java:

### 1. Báo cáo độc lập HTML (Mở được ngay trên máy tính)
Sau khi chạy test, file báo cáo HTML sẽ được tạo tự động tại:
`reports/report.html`
Bạn chỉ cần click đúp chuột vào file này để mở trên bất kỳ trình duyệt nào mà không cần cài đặt thêm phần mềm.

### 2. Allure Report (Dashboard đồ thị & timeline)
Sau khi chạy test, dữ liệu được ghi vào `reports/allure-results`.
Để hiển thị dashboard đồ thị Allure trên máy tính:
```bash
# Yêu cầu máy đã cài Allure CLI: https://allurereport.org/docs/install/
allure serve reports/allure-results
```

---

## 🚀 Đường ống CI/CD GitHub Actions

Quy trình tự động hóa được thiết lập tại `.github/workflows/ci.yml`:
1. **Trigger**: Tự động kích hoạt mỗi khi có code mới `push` hoặc tạo `pull_request` vào nhánh `main`.
2. **Environment**: Máy chủ ảo `ubuntu-latest` cài sẵn Google Chrome Headless và Python 3.12.
3. **Execution**: Tự động cài đặt dependencies và thực thi toàn bộ 15 test cases.
4. **Artifacts & Publish**:
   - Tự động đóng gói và lưu trữ file `pytest-html-report`.
   - Tự động tổng hợp và sinh `allure-html-report`.
   - Tự động triển khai báo cáo lên **GitHub Pages** để xem trực tuyến qua đường link web.

---

## 💻 Hướng dẫn chạy kiểm thử

```bash
# 1. Chạy toàn bộ test và tự động sinh cả 2 loại báo cáo (Headless):
pytest -v

# 2. Chạy có mở trình duyệt trực quan:
pytest -v --headed

# 3. Chạy riêng nhóm kiểm thử bảo mật:
pytest -m security -v
```
