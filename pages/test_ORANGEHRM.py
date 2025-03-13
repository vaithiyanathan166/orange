# from File Name import Class Name
from OrangeHRM import OrangeHRMAutomation
from OrangeHRM import Data
import pytest


# creating object from
orangeHrm = OrangeHRMAutomation(Data().url)

def test_start():
    assert orangeHrm.start() == True
    print("SUCCESS : Automation Started")


def test_validate_username_box():
    assert orangeHrm.validate_username_input_box() == True
    print("SUCCESS : Username Input Box is Visible")


def test_validate_password_box():
    assert orangeHrm.validate_password_input_box() == True
    print("SUCCESS : Password Input Box is Visible")


def test_validate_login_button():
    assert orangeHrm.validate_login_button() == True
    print("SUCCESS : Login Button is enabled")


def test_validate_login():
    assert orangeHrm.validate_login() == Data().dashboard_url
    print("SUCCESS : Login Success and Redirected to Dashboard Page")
