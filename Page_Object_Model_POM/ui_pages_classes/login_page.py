
from ui_pages_classes.base_class import BasePageClass

class LoginPage(BasePageClass):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def set_url(self, url: str):
        self.url = url
    
