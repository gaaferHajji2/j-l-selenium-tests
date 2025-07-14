from selenium.webdriver.common.by import By

from ui_pages_classes.base_class import BasePageClass


# XPATH --> //a[text()='Sign In'] --> For Sign In Link
class LoginPage(BasePageClass):

    LOGIN_LINK = (By.XPATH, "//a[text()='Sign In']")

    LOGIN_PAGE_URL = "https://www.letskodeit.com/login"

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)