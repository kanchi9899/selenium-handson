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
import random

def generate_email():
    return f"testuser{random.randint(1000,9999)}@example.com"

def generate_name():
    return f"testuser{random.randint(abcde,wedmfk)}@example.com"

# Navigate to URL
driver.get("https://automationexercise.com/")

# Use correct selector
element = driver.find_element(By.CSS_SELECTOR, ".logo.pull-left")
assert element.is_displayed()

print("Element found and displayed.")

#Click on signup/login
driver.find_element(By.LINK_TEXT, "Signup / Login" ).click()

#Verify that New User signup is visible
element = driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
assert element.is_displayed()

print("Signup/login is visible.")

# First attempt with a static user (already existing email)
name = "TestUser"
email = "testuser@example.com"

new_email = generate_email()
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-name"]').send_keys(name)
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-email"]').send_keys(new_email)
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()
time.sleep(5)

# Verify that 'ENTER ACCOUNT INFORMATION' is visible
element = driver.find_element(By.CSS_SELECTOR, ".title")
assert element.is_displayed()

print("Enter account information is visible")

#Filling the details
driver.find_element(By.CSS_SELECTOR, "#id_gender2").click()
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# # driver.find_element(By.CSS_SELECTOR, "#email").send_keys(new_email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Test@123")
driver.find_element(By.CSS_SELECTOR, "#days")

day_dropdown = driver.find_element(By.ID, "days")  # or By.CSS_SELECTOR, etc.
select_day = Select(day_dropdown)  # create a Select instance
select_day.select_by_value("9")    # call the method on the instance
day_dropdown = driver.find_element(By.ID, "months")
select_day = Select(day_dropdown)
select_day.select_by_value("8")
day_dropdown = driver.find_element(By.ID, "years")
select_day = Select(day_dropdown)
select_day.select_by_value("1999")
checkbox = driver.find_element(By.ID, "newsletter")
checkbox.click()

driver.find_element(By.CSS_SELECTOR, '[data-qa="first_name"]').send_keys("Test")
driver.find_element(By.CSS_SELECTOR, '[data-qa="last_name"]').send_keys("User")

country_dropdown = driver.find_element(By.ID, "country")
select_country = Select(country_dropdown)
select_country.select_by_value("India")

driver.find_element(By.CSS_SELECTOR, '[data-qa="address"]').send_keys("User testing address")
driver.find_element(By.CSS_SELECTOR, '[data-qa="state"]').send_keys("Gujarat")
driver.find_element(By.ID, 'city').send_keys("Surat")
driver.find_element(By.ID, 'zipcode').send_keys("367786")
driver.find_element(By.ID, 'mobile_number').send_keys("985625874")
driver.find_element(By.CSS_SELECTOR, '[data-qa="create-account"]').click()

element = driver.find_element(By.CLASS_NAME, "title")
assert element.is_displayed()
print("Account created.")

driver.find_element(By.CSS_SELECTOR, '[data-qa="continue-button"]').click()

time.sleep(5)

driver.quit()
