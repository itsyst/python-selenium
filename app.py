from selenium import webdriver
import config


browser = webdriver.Chrome()
browser.get(config.url)