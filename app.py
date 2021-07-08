from selenium import webdriver
import config


browser = webdriver.Firefox(executable_path=config.fox_path)
browser.get(config.url)
