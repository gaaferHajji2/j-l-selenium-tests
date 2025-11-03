from selenium import webdriver;
from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

import time;

service = Service(executable_path='chromedriver.exe');

driver = webdriver.Chrome(service=service);

driver.maximize_window();

driver.get("https://www.letskodeit.com/practice");

w1 = driver.current_window_handle;

print("The W1 Is: ", w1);

t1 = driver.find_element(By.ID, 'openwindow');

t1.click();

w2 = driver.window_handles;

print("The W2 Is: ", str(w2));

for w in w2:
    if w not in w1:
        driver.switch_to.window(w);
        print("Switch To Window: ", w);
        break;

t2 = WebDriverWait(driver=driver, timeout=25, poll_frequency=1).until(
    EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
)
# print("The T2 Is: ", t2);
# print("The T2 Is: ", t2.is_enabled());
# print("The T2 Is: ", t2.is_selected());
t2.send_keys("Python");

time.sleep(3);

driver.switch_to.window(w1);

driver.quit();