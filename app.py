from os import error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import config


browser = webdriver.Firefox(executable_path=config.fox_path)
browser.get(config.url)

sign_in_field = browser.find_element_by_link_text("Sign in")
sign_in_field.click()

username_field = browser.find_element_by_id("login_field")
username_field.send_keys(config.username)

password_field = browser.find_element_by_id("password")
password_field.send_keys(config.password)
password_field.submit()

# assert config.username in browser.page_source
try:
    profile_link = WebDriverWait(driver=browser, timeout=20, poll_frequency=1).until(
        EC.presence_of_element_located((By.CLASS_NAME, "user-profile-link")))

    link_label = profile_link.get_attribute("innerHTML")
    assert config.username in link_label
except TimeoutException:
    print("Time-out")
finally:
    browser.quit()
