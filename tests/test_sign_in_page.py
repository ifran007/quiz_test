import unittest
from tests.base_test import BaseTest
from pages.login_page import LoginPage


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
# just click right button of your mouse or mouse pad and click run button(pycharm)
class TestSignInPage(BaseTest):

    def test_sign_in_page(self):
        login_page = LoginPage(self.driver)
        login_page.login()


    
