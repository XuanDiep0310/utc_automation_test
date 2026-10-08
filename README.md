# UTC E-Office (vanphongdientu.utc.edu.vn) - Automation Testing Framework

Du an kiem thu tu dong (Automation Testing) cho phan he Dang nhap cua he thong Van phong dien tu Truong Dai hoc Giao thong van tai (UTC) tai dia chi: https://vanphongdientu.utc.edu.vn/

Du an duoc xay dung theo chuan cong nghiep Page Object Model (POM) ket hop voi Pytest, Selenium WebDriver, he thong bao cao Allure Report, Pytest-HTML va tich hop CI/CD GitHub Actions.

---

## Cau truc du an (Architecture)

```text
utc_automation_test/
|-- base/                                   # CAC LOP CO SO DUNG CHUNG
|   |-- __init__.py
|   |-- base_page.py                        # BasePage: thao tac chung (wait, click, type, alert, screenshot)
|   |-- base_test.py                        # BaseTest: khoi tao WebDriver, timeout, fixture ke thua
|-- pages/                                  # CAC PAGE OBJECTS (POM)
|   |-- __init__.py
|   |-- login_page.py                       # LoginPage: Form dang nhap, ke thua tu BasePage
|   |-- dashboard_page.py                   # DashboardPage: Menu, Header, thong tin user sau dang nhap
|-- tests/                                  # CAC TEST SCRIPTS (PYTEST & ALLURE)
|   |-- __init__.py
|   |-- conftest.py                         # Fixtures WebDriver, Allure screenshot on failure
|   |-- test_tc01_empty_username.py         # TC01: Kiem tra de trong ten dang nhap
|   |-- test_tc02_empty_password.py         # TC02: Kiem tra de trong mat khau
|   |-- test_tc03_correct_user_wrong_pass.py# TC03: Dung ten sai mat khau
|   |-- test_tc04_wrong_user_correct_pass.py# TC04: Sai ten dung mat khau
|   |-- test_tc05_login_persistent.py       # TC05: Dang nhap co chon 'Giu toi luon dang nhap'
|   |-- test_tc06_login_non_persistent.py   # TC06: Dang nhap khong chon 'Giu toi luon dang nhap'
|   |-- test_tc07_sql_injection_username.py # TC07: Security - SQL Injection bypass tren Username
|   |-- test_tc08_sql_injection_password.py # TC08: Security - SQL Injection bypass tren Password
|   |-- test_tc09_sql_injection_union.py    # TC09: Security - Union SQL Injection khai thac CSDL
|   |-- test_tc10_xss_script_injection.py   # TC10: Security - Cross-Site Scripting qua the script
|   |-- test_tc11_xss_html_injection.py     # TC11: Security - HTML Event Injection qua the onerror
|   |-- test_tc12_rate_limit_dos_resilience.py # TC12: Security - Kiem tra chiu tai don dap (Anti-DoS)
|   |-- test_tc13_password_masking.py       # TC13: Security - Che giau ky tu mat khau (type='password')
|   |-- test_tc14_boundary_long_input.py    # TC14: Security - Kiem tra chuoi cuc dai 5000 ky tu
|   |-- test_tc15_https_security.py         # TC15: Security - Kiem tra giao thuc HTTPS & SSL
|-- .github/
|   |-- workflows/
|       |-- ci.yml                          # Pipeline CI/CD GitHub Actions tu dong chay va tao Allure Report
|-- testcases/
|   |-- testcases_vanphongdientu.xlsx       # File Excel gom Bang quyet dinh va 15 Test Cases chi tiet
|-- reports/                                # Thu muc chua bao cao sau khi thuc thi
|   |-- report.html                         # Bao cao HTML truc quan (pytest-html)
|   |-- allure-results/                     # Du lieu sinh bao cao Allure Report
|-- serve_report.py                         # Script mo web server xem bao cao truc tiep tren trinh duyet
|-- generate_excel.py                       # Script sinh file Excel testcase tu dong
|-- pytest.ini                              # Cau hinh pytest, markers, alluredir, html report
|-- requirements.txt                        # Danh sach thu vien phu thuoc
|-- README.md
```

---

## Bao cao Kiem thu: Allure Report va HTML Report

Du an ho tro 2 dang bao cao chuyen nghiep:

### 1. Bao cao doc lap HTML (Mo truc tiep tren may tinh)
Sau khi chay test, file bao cao HTML duoc tao tai:
`reports/report.html`
Ban co the mo file nay truc tiep tren bat ky trinh duyet nao hoac chay lenh:
```bash
python serve_report.py
```
Server se mo cong 8080 va tu dong mo trinh duyet xem bao cao tai: `http://localhost:8080/report.html`

### 2. Allure Report (Dashboard do thi va timeline)
Sau khi chay test, du lieu duoc ghi vao `reports/allure-results`.
De hien thi dashboard do thi Allure tren may tinh:
```bash
allure serve reports/allure-results
```

---

## Duong ong CI/CD GitHub Actions

Quy trinh tu dong hoa duoc thiet lap tai `.github/workflows/ci.yml`:
1. Trigger: Tu dong kich hoat moi khi co code moi push hoac tao pull_request vao nhanh main.
2. Environment: May chu ao ubuntu-latest cai san Google Chrome Headless va Python 3.12.
3. Execution: Tu dong cai dat dependencies va thuc thi toan bo 15 test cases.
4. Artifacts va Publish:
   - Tu dong dong goi va luu tru file pytest-html-report.
   - Tu dong tong hop va sinh allure-html-report.
   - Tu dong trien khai bao cao len GitHub Pages de xem truc tuyen qua duong link web.

---

## Huong dan chay kiem thu

```bash
# 1. Chay toan bo test va tu dong sinh ca 2 loai bao cao (Headless):
pytest -v

# 2. Chay co mo trinh duyet truc quan:
pytest -v --headed

# 3. Chay rieng nhom kiem thu bao mat:
pytest -m security -v

# 4. Mo cong web xem bao cao ngay:
python serve_report.py
```
