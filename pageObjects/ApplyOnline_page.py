import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains, Keys
import ValueManager



class ApplyOnlinePage:
    __submitBtn = (By.XPATH, "//input[@id='nextBtn']")
    __GlobalError = (By.XPATH, "//div[@role='alert']")
    __FnameError = (By.XPATH, "//span[@for='candidate_first_name']")
    __LnameError = (By.XPATH, "//span[@for='candidate_last_name']")
    __EmailError = (By.XPATH, "//span[@for='candidate_email']")
    __PhoneError = (By.XPATH, "//span[@for='candidate_phone']")
    __CoverletterError = (By.XPATH, "//span[@for='cover-letter']")
    __CVError = (By.XPATH, "//span[@for='resume']")
    __DOBError = (By.XPATH, "//span[@for='date_of_birth']")
    __EducationError = (By.XPATH, "//span[@for='educational_qualification']")
    __CCEmployeeRadio = (By.XPATH, "//span[normalize-space()='CC employee']")
    __CCEmployeeError = (By.XPATH, "//span[@for='current_referrer_name']")
    __CityError = (By.XPATH, "//span[@for='city']")
    __StateError = (By.XPATH, "//span[@for='state']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def open(self):
        self._driver.get(ValueManager.dotNetFormUrl)

    def click_nextBtn(self):
        self._driver.find_element(*self.__submitBtn).click()

    def click_radioBtn(self):
        self._driver.find_element(*self.__CCEmployeeRadio).click()

    @property
    def error_FnameTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__FnameError))
        return self._driver.find_element(*self.__FnameError).get_attribute("data-empty-error")

    @property
    def error_LnameTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__LnameError))
        return self._driver.find_element(*self.__LnameError).get_attribute("data-empty-error")

    @property
    def error_EmailTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__EmailError))
        return self._driver.find_element(*self.__EmailError).text

    @property
    def error_PhoneTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__PhoneError))
        return self._driver.find_element(*self.__PhoneError).text

    @property
    def error_DOBTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__DOBError))
        return self._driver.find_element(*self.__DOBError).get_attribute("data-empty-error")

    @property
    def error_EducationTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__EducationError))
        return self._driver.find_element(*self.__EducationError).get_attribute("data-empty-error")

    @property
    def error_CoverletterTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__CoverletterError))
        return self._driver.find_element(*self.__CoverletterError).get_attribute("data-error")

    @property
    def error_CVTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__CVError))
        return self._driver.find_element(*self.__CVError).get_attribute("data-error")

    @property
    def error_CityTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__CityError))
        return self._driver.find_element(*self.__CityError).get_attribute("data-empty-error")

    @property
    def error_StateTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__StateError))
        return self._driver.find_element(*self.__StateError).get_attribute("data-empty-error")

    @property
    def error_CCEmployeeTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__CCEmployeeError))
        return self._driver.find_element(*self.__CCEmployeeError).get_attribute("data-empty-error")

    @property
    def error_GlobalTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__GlobalError))
        return self._driver.find_element(*self.__GlobalError).text

