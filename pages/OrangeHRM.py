from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


# Data Class to store the url
class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


# Locators Class to store all the web locators
class Locators:
    username_input_box = "username" # Name Locator
    password_input_box = "password" # Name Locator
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' # XPath Locator




class OrangeHRMAutomation:


    def __init__(self, web_url):
        self.url = web_url


        # code for using headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')


        # chromer driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


   
    def start(self):
        self.driver.get(self.url)
        sleep(5)
        return True
   
    def shutdown(self):
        self.driver.close()
   
    def validate_username_input_box(self):
        username_input_box_element = self.driver.find_element(by=By.NAME, value=Locators().username_input_box)
        if username_input_box_element.is_displayed():
            return True
        else:
            return False
       
   
    def validate_password_input_box(self):
        password_input_box_element = self.driver.find_element(by=By.NAME, value=Locators().password_input_box)
        if password_input_box_element.is_displayed():
            return True
        else:
            return False
       
   
    def validate_login_button(self):
        login_button_element = self.driver.find_element(by=By.XPATH, value=Locators().login_button)
        if login_button_element.is_enabled():
            return True
        else:
            return False
       
   
    def validate_login(self):
        self.driver.find_element(by=By.NAME, value=Locators().username_input_box).send_keys(Data().username)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=Locators().password_input_box).send_keys(Data().password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=Locators().login_button).click()
        sleep(5)
        if self.driver.current_url == Data().dashboard_url:
            return self.driver.current_url
        else:
            return False
