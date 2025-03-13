from selenium.webdriver.common.by import By
from base_page import BasePage

class AdminPage(BasePage):
    ADD_USER_BUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Confirm Password']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def create_new_user(self, username, password):
        self.click_element(self.ADD_USER_BUTTON)
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, password)
        self.click_element(self.SAVE_BUTTON)
