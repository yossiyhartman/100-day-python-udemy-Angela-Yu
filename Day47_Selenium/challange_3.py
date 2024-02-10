from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)

# run
driver.get("http://secure-retreat-92358.herokuapp.com/")

# form
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
signup = driver.find_element(By.TAG_NAME, value="button")

# fill in
first_name.send_keys("yossi")
last_name.send_keys("hartman")
email.send_keys("test@test.nl")

# subscribe
signup.click()
