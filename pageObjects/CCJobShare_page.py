import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import ValueManager
from ValueManager import openPositionUrl


class CCJobSharePage:

    __linkedInUsername = (By.XPATH, "//input[@id='session_key']")
    __linkedInPass = (By.XPATH, "//input[@id='session_password']")
    __linkednInSignInBtn = (By.XPATH, "//button[@type='submit'][normalize-space()='Sign in']")

    __post = (By.XPATH, "//div[@data-title='.NET Developer/ Senior Developer']")
    __linkedIn = (By.XPATH, "//a[@class='click-linkedin-share']")
    __facebook = (By.XPATH, "//a[@class='click-messenger-share']")
    __whatsapp = (By.XPATH, "//a[@class='click-whatsapp-share']")
    __copyLink = (By.XPATH, "//a[@class='click-copy-link']")

    __linkedInShareBtn = (By.XPATH, "//span[normalize-space()='Share in a post']")
    __linkedInPostImg = (By.ID, "ember62")
    __linkedInPostBtn = (By.XPATH, "//button[@id='ember53']")
    __linkedInViewPostBtn = (By.XPATH, "//a[normalize-space()='View post']")

    __linkedInImgAfterPosted = (By.XPATH, "//a[@aria-label='Open article: .NET Developer/ Senior Developer - Creative Capsule by creativecapsule.com']")


    def __init__(self, driver: WebDriver):
        self._driver = driver



    @property
    def current_url(self):
        return self._driver.current_url


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
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedInShareBtn))
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
        self._driver.save_screenshot(ValueManager.save_screenshot_path_linkedin)
        self._driver.find_element(*self.__linkedInImgAfterPosted).click()
        self._driver.switch_to.window(self._driver.window_handles[3])
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedIn))






