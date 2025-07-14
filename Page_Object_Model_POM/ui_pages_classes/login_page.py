
from ui_pages_classes import base_class

class LoginPage(base_class):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def set_url(self, url: str):
        self.url = url
    
