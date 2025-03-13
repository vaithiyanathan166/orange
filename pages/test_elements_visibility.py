#import pytest  # Import pytest
#from login_page import LoginPage

#@pytest.mark.usefixtures("driver")
#class TestElementsVisibility:
    #def test_login_elements(self, driver):
        #login_page = LoginPage(driver)
        #login_page.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #assert login_page.find_element(LoginPage.USERNAME_INPUT).is_displayed()
        #assert login_page.find_element(LoginPage.PASSWORD_INPUT).is_displayed()
