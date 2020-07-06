from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Disable browser based alerts
# 1- to enable
# 2 - to disable
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


class Bot:
    def __init__(self, email, password, webd=Chrome):
        self.driver = Chrome(options=option)
        self.email = email
        self.password = password

    def login(self):
        self.driver.get('https://www.facebook.com/')
        email = self.driver.find_element_by_id(
            'email').send_keys(self.email)
        password = self.driver.find_element_by_id(
            'pass').send_keys(self.password, Keys.RETURN)
        time.sleep(5)

    def message_to(self, username):
        self.driver.get(f'https://www.facebook.com/messages/t/{username}')
        time.sleep(5)

        with open('text2.txt', 'r') as file:
            for word in file.readlines():
                run = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, '_1mf'))).send_keys(word, Keys.RETURN)
                print(word)

    def close_browser(self):
        self.driver.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
