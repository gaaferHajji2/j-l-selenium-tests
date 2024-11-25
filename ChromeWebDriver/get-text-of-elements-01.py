from selenium import webdriver;

from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

from selenium.webdriver.support.ui import WebDriverWait;

from selenium.webdriver.support import expected_conditions as EC;


service = Service(executable_path='chromedriver.exe');

driver = webdriver.Chrome(service=service);

driver.maximize_window();

driver.get("https://www.letskodeit.com/practice");

WebDriverWait(driver=driver, timeout=15).until(
    EC.presence_of_element_located((
        By.XPATH, '//table[@id="product"]'
    ))
);

text_element = driver.find_element(
    By.XPATH, 
    "//table[@id='product']/tbody/tr[2]/td[@class='course-name']"
);

print("The Text Element Is: ", text_element);
print("The Content Of Text Element Is: ", text_element.text);

driver.quit();