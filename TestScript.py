# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://127.0.0.1:8000")


driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.ID, value="WebsiteName")
text_box2 = driver.find_element(by=By.ID, value="email")
submit_button = driver.find_element(by=By.NAME, value="GeneratePassword")

driver.implicitly_wait(0.5)

text_box.send_keys("Selenium")
text_box2.send_keys("Selenium12@gmail.com")
submit_button.click()

textBox3 = driver.find_element(by=By.ID, value="passwordtext")
value = textBox3.get_attribute("value")
driver.implicitly_wait(0.5)
print(value)

# message = driver.find_element(by=By.ID, value="message")
# value = message.text
# print(value)

# assert value == "Received!"
driver.quit()
