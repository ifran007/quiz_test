from utils.locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version

    def login(self):
        self.find_element(*self.locator.user_name).send_keys("SomeUser_name")
        self.find_element(*self.locator.password).send_keys("TopSecret1234!")
        self.find_element(*self.locator.login_btn).click()
        self.find_element(*self.locator.logout_btn).is_displayed()
        print(" ")
        print("Logged in successfully !")
        self.find_element(*self.locator.logout_btn).click()
        print("Logged out successfully !")


    # def logout(self):
    #     self.find_element(*self.locator.logout_btn).click()
        



    
