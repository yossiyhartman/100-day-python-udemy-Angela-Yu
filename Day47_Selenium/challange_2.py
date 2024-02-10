import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)

# run
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# menu
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text


searchbar = driver.find_element(By.NAME, value="search")

searchbar.send_keys("python", Keys.ENTER)

print(article_count)
