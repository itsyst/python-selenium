from selenium import webdriver
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

assert config.username in browser.page_source