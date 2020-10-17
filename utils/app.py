from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

'''
  Webdriver downloading according too chrome version ( hey nobody uses firefox so i am removing it from everywhere)
'''
from webdriver_manager.chrome import ChromeDriverManager


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
    def __init__(self, email, password):
        self.driver = Chrome(ChromeDriverManager().install())  # automatically install chrome driver acc to os default chrome version
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
        time.sleep(20)    # showing regular TIMEOUT in 5 secs so changed it to 20 secs
        try:
            with open('text.txt', 'r') as file:
                for word in file.readlines():
                    run = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, '_1mf'))).send_keys(word, Keys.RETURN)
                    print(word)
        except TimeoutException:     #please check this its always giving TimeOuts errors
            print("TimeoutException:  Something went wrong. Please try again.")

    def close_browser(self):
        self.driver.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
