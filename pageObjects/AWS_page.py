import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import ValueManager


class AWSPage:
    __left_arrow = (By.XPATH, "//a[@class='left carousel-control']//*[name()='svg']")
    __right_arrow = (By.XPATH, "//a[@class='right carousel-control']//*[name()='svg']")

    __WillMetcalf_text =(By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Will Metcalf')]")
    __SethLaskarzewski_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Seth Laskarzewski')]")
    __BillyTiller_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Billy Tiller')]")
    __JonathanPruitt_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Jonathan Pruitt')]")
    __AdiWalavalkar_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Adi Walavalkar')]")
    __HarrisonProffitt_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Harrison Proffitt')]")
    __JonathanPage_text = (By.XPATH, "//h4[@class='author-name mt-15 mb-0']//strong[contains(text(),'Jonathan Page')]")

    __aws_client_div = (By.XPATH, "//h2[normalize-space()='AWS Clients']")

    __WillMetcalf_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Will Metcalf – Senior Product Manager, PlanIT Impact']")
    __SethLaskarzewski_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Seth Laskarzewski – Senior Director of Commercial and Medical IT, Alkermes']")
    __BillyTiller_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Billy Tiller – Co-Founder and CEO, Grower Information Services Coop']")
    # __MaxReinig_text = (By.XPATH, "")
    # __MaxReinig_img
    __JonathanPruitt_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Jonathan Pruitt – Senior Product Manager, Main Street Data']")
    __AdiWalavalkar_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Adi Walavalkar']")
    __HarrisonProffitt_img = (By.XPATH, "//div[@class='row text-center']//img[@title='Harrison Proffitt – Founder, Bungii']")
    __JonathanPage_img = (By.XPATH, "//div[@class='row text-center']//img[@title='jonathan-page-cognitive-command']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(ValueManager.AWSUrl)

    @property
    def current_url(self):
        return self._driver.current_url

    def scollToSlider(self):
        ActionChains(self._driver) \
            .scroll_to_element(self._driver.find_element(*self.__aws_client_div))\
            .perform()

    def click_leftArrow(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__left_arrow))
        self._driver.find_element(*self.__left_arrow).click()

    def click_rightArrow(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__right_arrow))
        self._driver.find_element(*self.__right_arrow).click()


    def is_WillMetcalf_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__WillMetcalf_img))
        PresenceOf_WillMetcalf_img =  self._driver.find_element(*self.__WillMetcalf_img)
        return PresenceOf_WillMetcalf_img.is_displayed()


    def is_SethLaskarzewski_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__SethLaskarzewski_img))
        PresenceOf_SethLaskarzewski_img =  self._driver.find_element(*self.__SethLaskarzewski_img)
        return PresenceOf_SethLaskarzewski_img.is_displayed()


    def is_BillyTiller_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__BillyTiller_img))
        PresenceOf_BillyTiller_img = self._driver.find_element(*self.__BillyTiller_img)
        return PresenceOf_BillyTiller_img.is_displayed()


    def is_JonathanPruitt_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__JonathanPruitt_img))
        PresenceOf_JonathanPruitt_img =  self._driver.find_element(*self.__JonathanPruitt_img)
        return PresenceOf_JonathanPruitt_img.is_displayed()


    def is_AdiWalavalkar_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__AdiWalavalkar_img))
        PresenceOf_AdiWalavalkar_img = self._driver.find_element(*self.__AdiWalavalkar_img)
        return PresenceOf_AdiWalavalkar_img.is_displayed()


    def is_HarrisonProffitt_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__HarrisonProffitt_img))
        PresenceOf_HarrisonProffitt_img = self._driver.find_element(*self.__HarrisonProffitt_img)
        return PresenceOf_HarrisonProffitt_img.is_displayed()


    def is_JonathanPage_img_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__JonathanPage_img))
        PresenceOf_JonathanPage_img = self._driver.find_element(*self.__JonathanPage_img)
        return PresenceOf_JonathanPage_img.is_displayed()


    def get_JonathanPage_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__JonathanPage_text))
        PresenceOf_JonathanPage_text = self._driver.find_element(*self.__JonathanPage_text)
        print(PresenceOf_JonathanPage_text.text)



    def get_HarrisonProffitt_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__HarrisonProffitt_text))
        PresenceOf_HarrisonProffitt_text = self._driver.find_element(*self.__HarrisonProffitt_text)
        # return PresenceOf_HarrisonProffitt_text.text
        print(PresenceOf_HarrisonProffitt_text.text)


    def get_AdiWalavalkar_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__AdiWalavalkar_text))
        PresenceOf_AdiWalavalkar_text = self._driver.find_element(*self.__AdiWalavalkar_text)
        # return PresenceOf_AdiWalavalkar_text.text
        print(PresenceOf_AdiWalavalkar_text.text)


    def get_BillyTiller_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__BillyTiller_text))
        PresenceOf_BillyTiller_text = self._driver.find_element(*self.__BillyTiller_text)
        print(PresenceOf_BillyTiller_text.text)


    def get_JonathanPruitt_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__JonathanPruitt_text))
        PresenceOf_JonathanPruitt_text = self._driver.find_element(*self.__JonathanPruitt_text)
        print(PresenceOf_JonathanPruitt_text.text)


    def get_WillMetcalf_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__WillMetcalf_text))
        PresenceOf_WillMetcalf_text = self._driver.find_element(*self.__WillMetcalf_text)
        print(PresenceOf_WillMetcalf_text.text)


    def get_SethLaskarzewski_txt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__SethLaskarzewski_text))
        PresenceOf_SethLaskarzewski_text = self._driver.find_element(*self.__SethLaskarzewski_text)
        print(PresenceOf_SethLaskarzewski_text.text)

    def check_presence(self):

        if self.is_JonathanPage_img_displayed:
            self.get_JonathanPage_txt()
            # assert self.get_JonathanPage_txt() == "Jonathan Page", "The text isnt matching"
            # print(PresenceOf_JonathanPage_text.text)


        if self.is_HarrisonProffitt_img_displayed:
            self.get_HarrisonProffitt_txt()
            # assert self.get_HarrisonProffitt_txt() == "Harrison Proffitt", "The text isnt matching"
            # print(PresenceOf_HarrisonProffitt_text.text)


        if self.is_AdiWalavalkar_img_displayed:
            self.get_AdiWalavalkar_txt()
            # assert self.get_AdiWalavalkar_txt() == "Adi Walavalkar", "The text isnt matching"
            # print(PresenceOf_AdiWalavalkar_text.text)


        if self.is_BillyTiller_img_displayed:
            self.get_BillyTiller_txt()
            # assert self.get_BillyTiller_txt() == "Billy Tiller", "The text isnt matching"
            # print( "The " + PresenceOf_BillyTiller_text.text + " is shown")


        if self.is_JonathanPruitt_img_displayed:
            self.get_JonathanPruitt_txt()
            # assert self.get_JonathanPruitt_txt == "Jonathan Pruitt", "The text isnt matching"
            # print( "The " + PresenceOf_JonathanPruitt_text.text + " is shown")


        if self.is_SethLaskarzewski_img_displayed:
            self.get_SethLaskarzewski_txt()
            # assert self.get_SethLaskarzewski_txt == "Seth Laskarzewski", "The text isnt matching"
            # print( "The " + PresenceOf_SethLaskarzewski_text.text + " is shown")


        if self.is_WillMetcalf_img_displayed:
            self.get_WillMetcalf_txt()
            # assert self.get_WillMetcalf_txt == "Will Metcalf", "The text isnt matching"
            # print( "The " + PresenceOf_WillMetcalf_text.text + " is shown")




