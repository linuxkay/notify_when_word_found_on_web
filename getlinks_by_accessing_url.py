#/usr/bin/python3
# Get links by accessing url
from selenium import webdriver
import time
import numpy as np
#import requests
from bs4 import BeautifulSoup
import io
import re


browser = webdriver.Chrome()
browser.get("https://www.catalog.update.microsoft.com/Search.aspx?q=KB4598457")

elem = browser.find_element_by_xpath('//*[@id="151315e6-b978-42fc-b0ce-6e5c78a69324"]')
# before clicking button to open popup, store the current window handle
main_window = browser.current_window_handle

# click whatever button it is to open popup

# after opening popup, change window handle
for handle in browser.window_handles:
    if handle != main_window:
        popup = handle
        browser.switch_to_window(popup)


print(browser.title) # Should now be the popup window

#elem.click()
#time.sleep(0.2)

elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
# show main page html
    print(elem.get_attribute("href"))
