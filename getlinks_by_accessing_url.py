#/usr/bin/python3
# Get links by accessing url
from selenium import webdriver
import time
import numpy as np
from bs4 import BeautifulSoup
import io
import re

browser = webdriver.Chrome()
# set target url.
browser.get("https://www.catalog.update.microsoft.com/Search.aspx?q=KB4598457")
# set static xpath
#elem = browser.find_element_by_xpath('//*[@id="151315e6-b978-42fc-b0ce-6e5c78a69324"]')

# set dynamic xpath
#elem = browser.find_element_by_xpath("//tr[td[contains(text(),'2021-06')] and td[contains(text(),'Download')]]/input").click()
elem = browser.find_element_by_class_name("resultsbottomBorder.resultspadding") and browser.find_element_by_name('2021-06 .NET 5.0.7 Security Update for x64 Client')

print(elem)

# before clicking button to open popup, store the current window handle
main_window = browser.current_window_handle

# click whatever button it is to open popup
elem.click()
# add some sleep if needed. Default value is 0.2sec
time.sleep(0.2)
allHandles = browser.window_handles
# print id of window handle 1
print(allHandles[0])
# print id of window handle 2
print(allHandles[1])
# after opening popup, change window handle
for handle in browser.window_handles:
    if handle != main_window:
        popup = handle
        # change window to handle2
        browser.switch_to.window(allHandles[1])

print(browser.title) # Should now be the popup window

# search href in loop
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
# show main page html
    print(elem.get_attribute("href"))
