from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaBot:
    def __init__(self, username, password, search):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

        self.login()
        self.search_user(search)

    def login(self):
        self.driver.get("https://instagram.com")
        sleep(2)

        # Log in to Instagram
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').send_keys(Keys.ENTER)
        sleep(3)

        # Handle pop-ups
        self.handle_popups()

    def handle_popups(self):
        try:
            not_now_button = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
            not_now_button.click()
            sleep(3)
        except Exception as e:
            print("No 'Not Now' button found: ", e)

        try:
            turn_on_notifications_button = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
            turn_on_notifications_button.click()
            sleep(3)
        except Exception as e:
            print("No 'Turn on Notifications' button found: ", e)

    def search_user(self, search):
        search_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys(search)
        sleep(4)

        # Click on the first result
        first_result = self.driver.find_element(By.CLASS_NAME, 'z556c')
        first_result.click()
        sleep(5)

    def bulk_follow(self):
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').send_keys(Keys.ENTER)
        sleep(3)

        scroll_box = self.driver.find_element(By.CSS_SELECTOR, "div[class='isgrP']")
        
        number_of_following = 100  # Set the number of followings here
        scrolling_times = (number_of_following / 4)
        scroll_count = int(scrolling_times + 5)

        for _ in range(scroll_count):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_box)
            sleep(2)
            buttons = self.driver.find_elements(By.XPATH, '//button[text()="Follow"]')
            for btn in buttons:
                if btn.text == 'Follow':
                    self.driver.execute_script("arguments[0].click();", btn)
                    sleep(1)

# Add the username, password, and search term
bot = InstaBot('your_username', 'your_password', 'search_term')
bot.bulk_follow()
