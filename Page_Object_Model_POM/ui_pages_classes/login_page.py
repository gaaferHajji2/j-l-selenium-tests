from selenium.webdriver.common.by import By

from ui_pages_classes.base_class import BasePageClass


# XPATH --> //a[text()='Sign In'] --> For Sign In Link
class LoginPage(BasePageClass):

    LOGIN_LINK = (By.XPATH, "//a[text()='Sign In']")
    EMAIL_ADDRESS = (By.XPATH, "//input[@placeholder='Email Address']")
    PASSWORD = (By.XPATH, "//input[@id='login-password']")
    LOGIN_PAGE_URL = "https://www.letskodeit.com/login"
    LOGIN_BTN = (By.XPATH, "//button[@id='login']")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)
    
    def enter_email_addr(self):
        self.send_keys(locator=self.EMAIL_ADDRESS, text="test@email.com")
    
    def enter_password(self):
        self.send_keys(locator=self.PASSWORD, text="abcabc")
    
    def click_login_btn(self):
        self.click(self.LOGIN_BTN)
        