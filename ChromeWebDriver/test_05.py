from selenium import webdriver;

from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

import time;

service = Service(executable_path="chromedriver.exe");

driver = webdriver.Chrome(service=service);

driver.get("https://google.com/");

search_element = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']");

search_element.send_keys("Testing Using Selenium And BS4");

search_btn = driver.find_element(By.XPATH, "//div[@class='lJ9FBc']//input[@value='Google Search']");

search_btn.click();

time.sleep(10);

print("The Current Page URL Is: ", driver.current_url);

driver.quit();