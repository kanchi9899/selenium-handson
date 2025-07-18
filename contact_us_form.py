import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# Set Chrome options
options = Options()
options.add_argument("--incognito")  # Start in incognito mode (no cache)
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.maximize_window()

# Navigate to URL
driver.get("https://automationexercise.com/")

element = driver.find_element(By.CSS_SELECTOR, ".logo.pull-left")
assert element.is_displayed()

print("Home page is visible.")

#click on contact us
driver.find_element(By.CLASS_NAME, "fa-envelope").click()

element = driver.find_element(By.CLASS_NAME, "text-center")
assert element.is_displayed()

driver.find_element(By.CSS_SELECTOR, '[data-qa="name"]').send_keys("Testuser")
driver.find_element(By.CSS_SELECTOR, '[data-qa="email"]').send_keys("testuser@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[data-qa="subject"]').send_keys("Product quality")
driver.find_element(By.ID, "message").send_keys("Product quality is not good")
time.sleep(5)

# driver = webdriver.Chrome()
# driver.get("https://www.example.com/upload")

upload_input = driver.find_element(By.CSS_SELECTOR, 'input.form-control[type="file"]')
upload_input.send_keys(r"C:\Users\Kanchi\Downloads\Contract (1).pdf")  # Use raw string

driver.find_element(By.CSS_SELECTOR, '[data-qa="submit-button"]').click()
time.sleep(5)

alert = driver.switch_to.alert
alert.accept()

verify_success_message = driver.find_element(By.CLASS_NAME, "alert-success")
assert verify_success_message.is_displayed()

print("Success! Your details have been submitted successfully.")

driver.find_element(By.XPATH, '//a[text()=" Home"]')

element = driver.find_element(By.CSS_SELECTOR, ".logo.pull-left")
assert element.is_displayed()

print("Home page is visible.")