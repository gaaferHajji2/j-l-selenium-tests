from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import Tuple

class BasePageClass(ABC):

    def __init__(self, driver: webdriver.Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        
    def wait_for_element(self, locator: Tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator=locator))
    
    def click(self, locator: Tuple[str, str]):
        element = self.wait_for_element(locator=locator)
        element.click()
    
    def send_keys(self, locator: Tuple[str, str], text: str):
        element = self.driver.find_element(locator[0], locator[1])
        element.send_keys(text)