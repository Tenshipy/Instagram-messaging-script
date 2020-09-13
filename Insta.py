from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pg


class InstagramChat:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("Insert path to your => chromedriver.exe")
        self.login()

    def login(self):

        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        my_name = self.driver.find_element_by_name("username").send_keys(self.username)

        my_pass = self.driver.find_element_by_name("password").send_keys(self.password)

        log_click = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button'
        ).send_keys(Keys.ENTER)
        time.sleep(3)

        not_now = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        ).click()
        time.sleep(1)
        not_now2 = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]"
        ).click()
        time.sleep(2)

        message_icon = self.driver.find_element_by_class_name("xWeGp").click()
        time.sleep(2)
        send_message = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button'
        ).click()
        time.sleep(2)
        victim = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/div[2]/div[3]/div/div[1]"
        ).click()
        time.sleep(1)
        next = self.driver.find_element_by_class_name("rIacr").click()
        time.sleep(2)
        message_bar = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]'
        ).click()
        pg.typewrite("This is automated message lol!")
        pg.press("enter")

        time.sleep(60)
        self.driver.close()


if __name__ == "__main__":
    igbot = InstagramChat("your_username", "your_password")
