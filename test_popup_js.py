from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.catalog.update.microsoft.com/Search.aspx?q=KB4598457")

elem = browser.find_element_by_xpath('//*[@id="151315e6-b978-42fc-b0ce-6e5c78a69324"]')
elem.click()
time.sleep(0.2)

elem = browser.find_element_by_xpath("//*")
print(elem.get_attribute("outerHTML"))
