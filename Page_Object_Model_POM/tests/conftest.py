from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

import pytest

@pytest.fixture(scope='session')
def get_driver_and_web_wait():
    service = Service(executable_path='chromedriver.exe')

    driver = webdriver.Chrome(service=service)

    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1.0)

    yield driver, wait

    driver.quit()