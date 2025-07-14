
from ui_pages_classes.base_class import BasePageClass


# XPATH --> //a[text()="Sign In"] --> For Sign In Link
class LoginPage(BasePageClass):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
