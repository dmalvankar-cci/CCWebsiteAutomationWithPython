import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from globalConstants import openPositionUrl


class CCJobSharePage:

    __linkedInUsername = (By.ID, "username")
    __linkedInPass = (By.ID, "password")
    __linkednInSignInBtn = (By.XPATH, "//button[normalize-space()='Sign in']")

    __post = (By.XPATH, "//div[@data-title='.NET Developer/ Senior Developer']")
    __linkedIn = (By.XPATH, "//a[@class='click-linkedin-share']")
    __facebook = (By.XPATH, "//a[@class='click-messenger-share']")
    __whatsapp = (By.XPATH, "//a[@class='click-whatsapp-share']")
    __copyLink = (By.XPATH, "//a[@class='click-copy-link']")

    __linkedInShareBtn = (By.XPATH, "//span[normalize-space()='Share in a post']")
    __linkedInPostImg = (By.ID, "ember62")
    __linkedInPostBtn = (By.XPATH, "//button[@id='ember53']")
    __linkedInViewPostBtn = (By.XPATH, "//a[normalize-space()='View post']")


    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(openPositionUrl)

    def clickPost(self):
        self._driver.find_element(*self.__post).click()

    def clickLinkedInShare(self):
        self._driver.find_element(*self.__linkedIn).click()




    def linkedPostImg_isDisplayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedInPostImg))
        return self._driver.find_element(*self.__linkedInPostImg).is_displayed()

    def postToLinkedIn(self):
        self._driver.find_element(*self.__linkedInShareBtn).click()
    def afterOTGVerification(self):
        self._driver.find_element(*self.__linkedInPostBtn).click()
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedInViewPostBtn))
        self._driver.find_element(*self.__linkedInViewPostBtn).click()

    def perform_login(self, username, password):
        pass_username = self._driver.find_element(*self.__linkedInUsername)
        pass_password = self._driver.find_element(*self.__linkedInPass)
        press_loginBtn = self._driver.find_element(*self.__linkednInSignInBtn)

        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()

    def linkedinAfterSharing(self):
        self._driver.find_element(*self.__linkedInPostBtn).click()
        self._driver.save_full_page_screenshot("CCAfterSharing.png")





