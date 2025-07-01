from selenium import webdriver

from selenium.webdriver.chrome.service import Service

import pytest

@pytest.fixture(scope='session')
def get_chrome_driver():
    service = Service(executable_path='./chromedriver.exe');

    driver = webdriver.Chrome(service=service);

    return driver;