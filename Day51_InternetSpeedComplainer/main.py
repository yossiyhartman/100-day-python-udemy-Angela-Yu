import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
