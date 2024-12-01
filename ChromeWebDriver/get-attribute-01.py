from selenium import webdriver;

from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.support import expected_conditions as EC;

from selenium.webdriver.support.ui import WebDriverWait;

from selenium.webdriver.common.by import By;

service = Service(executable_path='chromedriver.exe');

driver = webdriver.Chrome(service=service);

driver.maximize_window();

driver.get("https://www.letskodeit.com/practice");

WebDriverWait(driver=driver, timeout=15).until(
    EC.presence_of_element_located((By.ID, 'name'))
);

name_element = driver.find_element(By.ID, 'name');

print("The Name Element Is: ", name_element);

name_element.send_keys('Jafar Loka');

elem_type = name_element.get_attribute('type');
elem_place_holder = name_element.get_attribute('placeholder');
elem_val = name_element.get_attribute('value');

driver.quit();