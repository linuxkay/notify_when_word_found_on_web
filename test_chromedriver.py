# - coding: utf-8 --
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://example.com/"

# ヘッドレスモードでブラウザを起動
options = ChromeOptions()
options.add_argument('--headless')

# サービスを起動
serv = Service(ChromeDriverManager().install())

# ブラウザーを起動
driver = webdriver.Chrome(service=serv, options=options)

# urlにアクセス
driver.get(url)
title = driver.find_element_by_tag_name("h1")
print(title.text)

# ブラウザ停止
driver.quit()
