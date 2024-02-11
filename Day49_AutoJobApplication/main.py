from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from secrets import config

# config
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)

# run
driver.get(
    url="https://www.linkedin.com/jobs/search/?currentJobId=3798127894&f_LF=f_AL&geoId=90010383&keywords=data%20engineer&location=Amsterdam%20Area&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
)


# steps

# 1. Sign in
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]").click()

# 2. Sign in with test account
time.sleep(3)
input_username = driver.find_element(By.CSS_SELECTOR, value="input#username")
input_password = driver.find_element(By.CSS_SELECTOR, value="input#password")
login_button = driver.find_element(
    By.CSS_SELECTOR, value=".login__form_action_container button"
)

input_username.send_keys(config["linkedin"]["email"])
input_password.send_keys(config["linkedin"]["password"])
login_button.click()


# here you're required to automatically apply for linkedIn jobs ..
# good exercise for later
