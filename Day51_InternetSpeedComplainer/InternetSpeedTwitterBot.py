from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException


class InternetSpeedTwitterBot:
    def __init__(self) -> None:

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        self.up = 600
        self.down = 50

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        # Deny cookies button
        cookie_button = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookies_wait = WebDriverWait(self.driver, timeout=10).until(
            lambda d: cookie_button.is_displayed()
        )
        cookie_button.click()

        # start internet test
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()

        ignore_app_download_button = self.driver.find_element(
            By.CSS_SELECTOR,
            "modal .close-button",
        )

        test_wait = WebDriverWait(
            self.driver,
            timeout=500,
            poll_frequency=10,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotInteractableException,
            ],
        ).until(lambda d: ignore_app_download_button.is_displayed())

        ignore_app_download_button.click()

        down = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        up = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text

        print("download {}, upload {}".format(down, up))

        return up, down
