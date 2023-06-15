import time
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys
import ValueManager
from ValueManager import openPositionUrl


class JobDescriptionsPage:

    __number_of_positions_txt = (By.XPATH, "//p[@class='open-position-text']")

    __google_search = (By.XPATH, "//textarea[@id='APjFqb']")
    __paste_text = (By.XPATH, "//span[contains(text(),'https://www.creativecapsule.com/vacancies/net-deve')]")

    __linkedInUsername = (By.ID, "username")
    __linkedInPass = (By.ID, "password")
    __linkednInSignInBtn = (By.XPATH, "//button[@type='submit'][normalize-space()='Sign in']")

    __fbUsername = (By.ID, "email")
    __fbPass = (By.ID, "pass")
    __fbLoginBtn = (By.ID, "loginbutton")
    __fb_enter_friend = (By.XPATH, "//input[@placeholder='Enter friends']")
    __fb_SamajikCci = (By.XPATH, "//li[@title='Saamajik Cci']")
    __send_fb_post = (By.NAME, "publish")
    __fb_messanger = (By.XPATH, "//div[@aria-label='Messenger']")

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

    __applyOnline_link = (By.XPATH, "//div[@class='apply-online-callout']//strong[contains(text(),'Apply online')]")
    __openPositions_link =(By.XPATH, "//p[@class='open-position-text']//strong[contains(text(),'Open Positions')]")
    __aboutUs_link = (By.XPATH, "//strong[normalize-space()='About Us']")
    __workingAtCC_link = (By.XPATH, "//strong[normalize-space()='Working at Creative Capsule']")
    __careerPath_link = (By.XPATH, "//strong[normalize-space()='Career Paths']")

    def __init__(self, driver: WebDriver):
        self._driver = driver



    @property
    def current_url(self):
        return self._driver.current_url


    def open(self):
        self._driver.get(openPositionUrl)

    def clickPost(self):
        self._driver.find_element(*self.__post).click()

    def click_send_fbPost(self):
        self._driver.find_element(*self.__send_fb_post).click()

    def click_aboutUs_link(self):
        self._driver.find_element(*self.__aboutUs_link).click()

    def click_workingAtCC_link(self):
        self._driver.find_element(*self.__workingAtCC_link).click()

    def click_careerPath_link(self):
        self._driver.find_element(*self.__careerPath_link).click()

    def click_openPositions_link(self):
        self._driver.find_element(*self.__openPositions_link).click()

    def click_applyOnline_link(self):
        self._driver.find_element(*self.__applyOnline_link).click()

    def clickLinkedInShare(self):
        self._driver.find_element(*self.__linkedIn).click()
    def click_fb_messanger(self):

        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fb_messanger))
        self._driver.find_element(*self.__fb_messanger).click()
        self._driver.save_screenshot(ValueManager.save_screenshot_path_FacebookShare)

    def click_FBShare(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__facebook))
        self._driver.find_element(*self.__facebook).click()

    def select_fb_friend(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fb_enter_friend))
        self._driver.find_element(*self.__fb_enter_friend).click()
        self._driver.find_element(*self.__fb_enter_friend).send_keys("saama")
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fb_SamajikCci))
        self._driver.find_element(*self.__fb_SamajikCci).click()

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

    def perform_login_fb(self, username, password):
        pass_username = self._driver.find_element(*self.__fbUsername)
        pass_password = self._driver.find_element(*self.__fbPass)
        press_loginBtn = self._driver.find_element(*self.__fbLoginBtn)

        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()

    def linkedinAfterSharing(self):
        self._driver.save_screenshot(ValueManager.save_screenshot_path_linkedin)
        self._driver.find_element(*self.__linkedInImgAfterPosted).click()
        self._driver.switch_to.window(self._driver.window_handles[3])
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedIn))

    def click_copyLink(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__copyLink))
        self._driver.find_element(*self.__copyLink).click()

    def pasteLink(self):
        self._driver.switch_to.new_window("Window")
        profile_window = self._driver.window_handles[1]
        self._driver.switch_to.window(profile_window)
        self._driver.get("https://google.com")
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__google_search))
        self._driver.find_element(*self.__google_search).click()
        action = ActionChains(self._driver)
        # action.key_down(Keys.CONTROL).send_keys('a').perform()
        # action.send_keys(Keys.DELETE).perform()
        action.send_keys(pyperclip.paste()).perform()
        action.send_keys(Keys.ENTER).perform()

    @property
    def getTextFromSearch(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__google_search))
        return self._driver.find_element(*self.__google_search).text


    def click_whatsapp_share(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__whatsapp))
        self._driver.find_element(*self.__whatsapp).click()
        profile_window = self._driver.window_handles[1]
        self._driver.switch_to.window(profile_window)
    @property
    def positionNumbersVerification(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__number_of_positions_txt))
        return self._driver.find_element(*self.__number_of_positions_txt).text











