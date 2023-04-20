import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class globalRedirectsRulePage:

    __CCLogo = (By.XPATH, "//a[@title='Creative Capsule']")

    __yahooTextArea = (By.ID, 'yschsp')
    __yahooBtn = (By.XPATH, "//button[@type='submit']")

    __bingLink = (By.LINK_TEXT, 'Software Consulting and Development - Creative Capsule')
    __yahooLink = (By.XPATH, "//a[contains(text(),'Software Consulting and Development - Creative Cap')]")


    __bingTextArea = (By.XPATH, "//textarea[@id='sb_form_q']")
    __bingBtn = (By.XPATH, "//label[@id='search_icon']//*[name()='svg']")

    __googleTextArea = (By.ID, 'APjFqb')
    __googleBtn = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
    __googleLink = (By.XPATH, "//h3[contains(text(),'Creative Capsule: Software Consulting and Developm')]")

    __googleUrl = "https://www.google.com/"
    __yahooUrl = "https://in.search.yahoo.com/"
    __bingUrl = "https://www.bing.com/"

    __url = "https://www.creativecapsule.com"

    # __Url = "www.creativecapsule.com"
    # # Global redirects
    # __url = "Creativecapsule.com"
    # __Url2 = "www.creativecapsule.com"
    # __Url3 = "http://www.creativecapsule.com"
    # __Url4 = "http://creativecapsule.com"
    # __Url5 = "https://creativecapsule.com"
    # __Url6 = "Creativecapsule.com/"
    # __Url7 = "CreativeCaPsuLe.com"
    # __Url8 = "creativecapsul.us"
    # __Url9 = "creativecapsule.us"
    # __Url10 = "creativecapsul.com"
    # __Url11 = "creativecapsule.ch"
    # __Url12 = "creativecapsule.net"
    # __Url13 = "creativecapsule.mobi"
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # def open(self):
    #     self._driver.get(self.__websiteUrl)
        # self._driver.switch_to.new_window('tab')

        # self._driver.get(self.__Url1)
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(ec.url_changes(self.__Url1))


        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url2)
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(ec.url_changes(self.__Url))
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url3)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url4)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url5)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url6)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url7)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url8)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url9)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url10)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url11)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url12)
        # self._driver.switch_to.new_window('tab')
        # self._driver.get(self.__Url13)





    @property
    def current_url(self):
        return self._driver.current_url


    def yahooSearch(self):
        self._driver.get(self.__yahooUrl)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__yahooTextArea))
        self._driver.find_element(*self.__yahooTextArea).send_keys("Creative capsule")
        self._driver.find_element(*self.__yahooBtn).click()

        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__yahooLink))
        self._driver.find_element(*self.__yahooLink).click()
        time.sleep(4)





    def bingSearch(self):
        self._driver.get(self.__bingUrl)
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__bingTextArea))
        TA = self._driver.find_element(*self.__bingTextArea)
        TA.click()
        time.sleep(1)
        TA.send_keys("Creative capsule")
        # For Firefox
        # TA.click()
        ActionChains(self._driver).send_keys(Keys.ENTER).perform()
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__bingLink))
        self._driver.find_element(*self.__bingLink).click()
        time.sleep(4)

    def googleSearch(self):
        # self._driver.switch_to.new_window('tab')
        self._driver.get(self.__googleUrl)
        self._driver.find_element(*self.__googleTextArea).send_keys("Creative capsule")
        self._driver.find_element(*self.__googleBtn)
        ActionChains(self._driver).send_keys(Keys.ENTER).perform()
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__googleLink))
        self._driver.find_element(*self.__googleLink).click()
        ActionChains(self._driver).send_keys(Keys.ENTER).perform()





