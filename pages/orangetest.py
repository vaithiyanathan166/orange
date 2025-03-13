import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
import os
from time import sleep
from login_page import LoginPage
from tests.Homepage import HomePage
from utilities.excel_function    import ExcelUtils
from utilities.report_generator import ReportGenerator

# Test configuration
@pytest.fixture(scope="session")
def setup_browser():
    """Set up the Selenium WebDriver."""
    options = Options()
    options.add_argument("--start-maximized")
    driver_service = Service("chromedriver")
    driver = webdriver.Chrome(service=driver_service, options=options)
    yield driver
    driver.quit()

# Utility functions
@pytest.fixture(scope="session")
def test_data():
    """Load test data from an Excel file."""
    excel_file = "test_data.xlsx"
    return ExcelUtils.load_test_data(excel_file)

# Test Cases
class TestOrangeHRM:
    @pytest.fixture(autouse=True)
    def setup_method(self, setup_browser):
        """Set up method for every test."""
        self.driver = setup_browser
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_login_logout(self, test_data):
        """Verify login and logout functionality using test data."""
        login_page = LoginPage(self.driver)
        for data in test_data:
            username, password, expected_result = data
            login_page.login(username, password)
            if expected_result == "success":
                assert login_page.is_logged_in(), "Login failed when it should have succeeded."
                login_page.logout()
                assert login_page.is_logged_out(), "Logout failed."
            else:
                assert not login_page.is_logged_in(), "Login succeeded when it should have failed."

    def test_home_url(self):
        """Verify whether the home URL is working."""
        current_url = self.driver.current_url
        assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "Home URL is incorrect."

    def test_input_boxes_visible(self):
        """Verify username and password input boxes visibility."""
        login_page = LoginPage(self.driver)
        assert login_page.are_input_boxes_visible(), "Input boxes are not visible."

    def test_menu_visibility(self):
        """Verify visibility and clickability of main menus after login."""
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        home_page = HomePage(self.driver)
        assert home_page.are_menus_visible(), "Menus are not visible."
        assert home_page.are_menus_clickable(), "Menus are not clickable."

    def test_create_new_user(self):
        """Create a new user and verify login functionality."""
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        home_page = HomePage(self.driver)
        home_page.navigate_to_admin_menu()
        new_user_details = {
            "username": "newuser",
            "password": "newpassword123"
        }
        home_page.create_user(new_user_details)
        login_page.logout()
        login_page.login(new_user_details["username"], new_user_details["password"])
        assert login_page.is_logged_in(), "New user login failed."

    def test_new_user_in_records(self):
        """Verify new user exists in the records."""
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        home_page = HomePage(self.driver)
        home_page.navigate_to_admin_menu()
        assert home_page.is_user_in_records("newuser"), "New user does not exist in records."
