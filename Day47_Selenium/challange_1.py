import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

# config
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)

# run
driver.get("https://www.python.org/")


# menu
menu = driver.find_element(
    By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
)

menu_items = menu.find_elements(By.CSS_SELECTOR, value="li")

events = {}

for i, li in enumerate(menu_items):
    date = li.find_element(By.TAG_NAME, value="time").get_attribute(name="datetime")
    date = date[:10]  # strip only the date
    event = li.find_element(By.TAG_NAME, value="a").text

    # add to event dictionairy
    events[i] = {"time": date, "event": event}

print(events)
driver.quit()
