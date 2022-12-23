# encoding:utf-8
from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('https://www.kadirli.bel.tr/yoresel-agiz/')
time.sleep(30)
search = browser.find_elements("tag name", "li")
for k in search:
    if len(k.text) > 0:
        print(k.text)
time.sleep(100000)