from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import randint
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_DRIVE_PATH = "/Applications/Development/chromedriver"

instagram_username = "" #your username
instagram_pass = "" #your pass

SCROLL_PAUSE_TIME = 0.5

class InstaFollower:
    def __init__(self):
        self.service = Service(CHROME_DRIVE_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(8)
        allow_cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        allow_cookies.click()

        time.sleep(8)

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(instagram_username)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(instagram_pass)

        password.send_keys(Keys.ENTER)

        time.sleep(8)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/nitescu.ruxandra/')

        time.sleep(5)
        followers_count = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_count.click()

        time.sleep(5)

        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        # To scroll down thrice in the followers pop-up.
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)


    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button ._aacl")
        # print(follow_buttons)
        follow_txt = [btn.text for btn in follow_buttons]
        print(follow_txt)

        for button in follow_buttons[2:]:
            print(button.text)

            if button.text == "Follow":
                button.click()
                time.sleep(2)


instagram_bot = InstaFollower()
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
