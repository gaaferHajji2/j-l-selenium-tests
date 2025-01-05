from selenium import webdriver;
from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

import time;

service = Service(executable_path='chromedriver.exe');

driver = webdriver.Chrome(service=service);

driver.maximize_window();

driver.get('https://www.letskodeit.com/');

login_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'SIGN IN');

login_element.click();

input_element_01 = WebDriverWait(driver=driver, timeout=15, poll_frequency=1).until(
    EC.presence_of_element_located((By.ID, 'email'))
);

input_element_01.send_keys("test@test.com");

input_element_02 = driver.find_element(By.ID, 'login-password');

input_element_02.send_keys("Test@123");

submit_btn = driver.find_element(By.ID, 'login');

submit_btn.click();

time.sleep(3);

dest_file_name = str(time.time()) + "_j-l-screen-shot.png";

try:
    driver.save_screenshot(dest_file_name);

    title = driver.execute_script("return document.title");

    print("The Title Of Document Is: ", title);

    height = driver.execute_script("return window.innerHeight;");
    width  = driver.execute_script("return window.innerWidth");

    print("The Height Of Window Is: " + str(height));
    print("The Width Of Window Is: " + str(width));
except Exception as e:
    print("The Error Is: ", e.__str__());