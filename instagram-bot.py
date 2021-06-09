from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import FirefoxOptions
from time import sleep


# setting options to run in headless mode (firefox)
# opts = FirefoxOptions()
# opts.add_argument("--headless")
# opts.add_argument("--localhost:0.0")
# browser = webdriver.Firefox(firefox_options=opts)

# PATH = "C:\Program Files\geckodriver.exe"
# driver.set_window_position(-1000, 0)
# driver.maximize_window()
# -------------------------------------------------
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://www.instagram.com/")
print(f'Driver initiated: {driver.title}. Hello, human! My name is Twip')

sleep(4)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_input = driver.find_element_by_name("username")
    username_input.send_keys("twip_the_twipper001")
    password_input = driver.find_element_by_name("password")
    password_input.send_keys("&[ypZ8cpy]k-")
    password_input.send_keys(Keys.RETURN)
    sleep(5)


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.instagram.com/")
    save_info_button = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div/div/button")
    save_info_button.click()
    notification_not_now = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div/div/div[3]/button[2]")
    notification_turn_on = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div/div/div[3]/button[1]")
    notification_turn_on.click()


# driver.close()
# print("Driver closed.")
