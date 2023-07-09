import selenium
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 100
PROMISED_UP = 10
TWITTER_EMAIL = "Your_email"
TWITTER_PASSWORD = "Your_password"
CHROME_DRIVER_PATH = "C:/Users/horyu/Development/chromedriver.exe"

class InternetspeedTwitterBot:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.download_mbps = 0
        self.upload_mbps = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.start = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.start.click()
        time.sleep(50)
        self.download_mbps = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload_mbps = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.download_mbps}")
        print(f"Up: {self.upload_mbps}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "text")
        email.send_keys("m-416369@moe-dl.edu.my")
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("biochemphy100%")
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.NAME, "text")
            username.send_keys("pythontestacc1")
            username.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("biochemphy100%")
            password.send_keys(Keys.ENTER)

        time.sleep(3)

        typing_box = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        typing_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_mbps} down/{self.upload_mbps} up when i pay for 60down/30up?")
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        submit_button.click()


driver = InternetspeedTwitterBot()
driver.get_internet_speed()
driver.tweet_at_provider()



