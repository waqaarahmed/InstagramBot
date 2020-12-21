from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaBot:
    def __init__(self, username, password, search):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_name("username")\
            .send_keys(username)
        self.driver.find_element_by_name("password")\
            .send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]')\
            .send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')\
            .send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.XPATH, '//button[text()="Not Now"]') \
            .send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(search)
        sleep(4)
        self.driver.find_element(By.CLASS_NAME, 'z556c')\
            .click()
        sleep(5)

    def bulk_follow(self):
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
            .send_keys(Keys.ENTER)
        sleep(3)
        scroll_box = self.driver.find_element_by_css_selector("div[class='isgrP']")
        # Add the number of followers of the user
        scrolling_times = (numberoffollowersoftheuser / 4)
        scroll = 0
        scroll_count = scrolling_times + 5  # You can use your own logic to scroll down till the bottom
        while scroll < scroll_count:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                scroll_box)
            sleep(2)
            buttons = self.driver.find_elements(By.XPATH, '//button[text()="Follow"]')
            for btn in buttons:
                if btn.text == 'Follow':
                    self.driver.execute_script("arguments[0].click();", btn)
                    sleep(1)
            scroll += 1


Bot = InstaBot('username', 'password', 'usernameforsearch')
Bot.bulk_follow()