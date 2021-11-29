from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):
    
    user_name = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/input[1]")
    password = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/input[2]")
    login_btn = (By.XPATH, "//button[contains(text(),'LOGIN')]")
    logout_btn = (By.XPATH, "//button[contains(text(),'LOGOUT')]")
