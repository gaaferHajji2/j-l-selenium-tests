from selenium import webdriver;

from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

service = Service(executable_path='chromedriver.exe');

driver = webdriver.Chrome(service=service);

driver.maximize_window();

driver.get("https://www.letskodeit.com/");

WebDriverWait(driver=driver, timeout=15).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/login"]'))
);

login_element = driver.find_element(By.XPATH, '//a[@href="/login"]');

print("The Login Element IS: ", login_element);

login_element.click();

print("The Current Page URL Is: ", driver.current_url);

driver.quit();