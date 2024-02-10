from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# config
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)

# run
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# items
money = driver.find_element(By.ID, value="money")
cookie = driver.find_element(By.ID, value="cookie")

store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrade_ids = [item.get_attribute("id") for item in store_items]

timeout = time.time() + 5
fivemin = time.time() + 60 * 5

# start the game
while True:
    # click that cookie
    cookie.click()

    if time.time() > fivemin:  # after 5 min stop the game
        break  # end game

    if time.time() > timeout:  # every 5 seconds buy an upgrade
        timeout = time.time() + 5

        # grab all current store prices
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        upgrade_cost = []

        # Clean prices
        for item in upgrades:
            if item.text != "":
                cost = int(item.text.split("-")[1].strip().replace(",", ""))
                upgrade_cost.append(cost)

        # merge cost & id's
        items = zip(upgrade_ids, upgrade_cost)

        # # current money
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

        # buy most expensive shit
        affordable = [id for id, cost in items if cost < money]

        if affordable != []:
            driver.find_element(By.ID, value=affordable[-1]).click()
