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

print("Element found and displayed.")

#Click on signup/login
driver.find_element(By.LINK_TEXT, "Signup / Login" ).click()

#Verify that New User login is visible
element = driver.find_element(By.CLASS_NAME, "login-form")
assert element.is_displayed()
time.sleep(5)

with open("user_credentials.txt", "r") as f:
    email, password = f.read().split(",")

driver.find_element(By.CSS_SELECTOR, '[data-qa="login-email"]').send_keys(email.strip())
driver.find_element(By.CSS_SELECTOR, '[data-qa="login-password"]').send_keys(password.strip())

driver.find_element(By.CSS_SELECTOR, '[data-qa="login-button"]').click()

login_user = driver.find_element(By.CSS_SELECTOR, "li a b")
assert login_user.is_displayed()
print("Login user is visible.")

driver.find_element(By.CSS_SELECTOR, 'a[href="/delete_account"]').click()
user_deleted = driver.find_element(By.CLASS_NAME, "title")
assert user_deleted.is_displayed()

time.sleep(5)

#Login user with incorrect username and password

#Click on signup/login
driver.find_element(By.LINK_TEXT, "Signup / Login" ).click()

#Verify that New User login is visible
element = driver.find_element(By.CLASS_NAME, "login-form")
assert element.is_displayed()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, '[data-qa="login-email"]').send_keys("tfgyd@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[data-qa="login-password"]').send_keys("Password")

driver.find_element(By.CSS_SELECTOR, '[data-qa="login-button"]').click()

error = driver.find_element(By.XPATH, "//p[contains(text(),'Your email or password is incorrect')]")
assert error.is_displayed()
print("Email or password is incorrect.")
time.sleep(5)