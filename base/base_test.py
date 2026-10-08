import pytest

class BaseTest:
    """
    BaseTest: Lớp cơ sở cho các kịch bản kiểm thử (Test Classes).
    Tương đương BaseTest.java trong kiến trúc Java/JUnit 5.
    Cung cấp quyền truy cập tới WebDriver và các Page Objects thông qua fixture.
    """
    @pytest.fixture(autouse=True)
    def setup_base(self, driver):
        self.driver = driver
