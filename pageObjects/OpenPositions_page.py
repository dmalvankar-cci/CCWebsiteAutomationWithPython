import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import ValueManager
from ValueManager import websiteUrl


class OpenPositionsPage:
    __open_positions = (By.LINK_TEXT, "Open Positions")

    __search_field = (By.XPATH, "//input[@id='search_job_title']")
    __search_close = (By.XPATH, "//button[@class='btn-close']//*[name()='svg']")

    __invalid_search_txt = (By.XPATH, "//div[@class='empty-block lg-screen d-none d-md-block']")
    __dotnetdev_txt = (By.XPATH, "//strong[normalize-space()='.NET Developer/ Senior Developer']")
    __application_link = (By.LINK_TEXT, "application")
    __placeholder_inTheSearchField = (By.XPATH, "//label[normalize-space()='Search Job Title']")

    __applyHere = (By.XPATH, "//a[@class='primary-link apply-here-link d-none d-md-inline-block']")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def click_openPositions_menu(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__open_positions))
        self._driver.find_element(*self.__open_positions).click()

    def invalidSearch(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__search_field))
        searchArea = self._driver.find_element(*self.__search_field)
        searchArea.click()
        searchArea.send_keys(ValueManager.invalidTextToPassInTheSearchField)

    def validSearch(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__search_field))
        searchArea = self._driver.find_element(*self.__search_field)
        searchArea.click()
        searchArea.send_keys(ValueManager.validTextToPassInTheSearchField)


    @property
    def verify_invalidSearchTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__invalid_search_txt))
        invalid_search_text = self._driver.find_element(*self.__invalid_search_txt)
        return  invalid_search_text.text

    @property
    def verify_dotNetTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dotnetdev_txt))
        dot_net_text = self._driver.find_element(*self.__dotnetdev_txt).text
        return dot_net_text


    def click_dotNet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dotnetdev_txt))
        self._driver.find_element(*self.__dotnetdev_txt).click()


    def click_searchClose(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__search_close))
        self._driver.find_element(*self.__search_close).click()

    def click_applicationLink(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__application_link))
        self._driver.find_element(*self.__application_link).click()

    @property
    def get_textFromSearchField(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__placeholder_inTheSearchField))
        textOfSearch = self._driver.find_element(*self.__placeholder_inTheSearchField)
        return textOfSearch.text

    def click_applyHere_link(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__applyHere))
        self._driver.find_element(*self.__applyHere).click()


