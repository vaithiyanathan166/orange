from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_login_successful(self):
        try:
            self.find_element((By.XPATH, "//h6[text()='Dashboard']"))
            return True
        except:
            return False
