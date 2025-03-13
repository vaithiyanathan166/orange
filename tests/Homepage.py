from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from time import sleep


class HRMLogin:
    #test data
    username = "Admin"
    password = "admin123"


    #test locators
    username_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    password_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'


    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()    
   
    def login(self):
        # maximize the window
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        # enter the username
        self.driver.find_element(by=By.XPATH, value=self.username_locator).send_keys(self.username)
        sleep(2)
        # enter the password
        self.driver.find_element(by=By.XPATH, value=self.password_locator).send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
        sleep(5)


        if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
            print("SUCCESS: TEST CASE PASSED")
            return True
        else:
            print("FAILED: TEST CASE FALED")
            return False
       
    def shutdown(self):
        self.driver.quit()
        return None
