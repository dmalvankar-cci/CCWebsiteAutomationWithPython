import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import ValueManager
from ValueManager import websiteUrl


class WorkingAtCCPage:
    __careers_menu = (By.ID, 'dropdown3196')
    __working_at_cc = (By.LINK_TEXT, 'Working at Creative Capsule')

    __training_education = (By.XPATH, "//div[@data-gtag-click-label='cc-workingatcc-newfutureatcc-card-trainingandeducation-clk']")
    __competitive_compensation = (By.XPATH, "//div[contains(@data-gtag-click-label,'cc-workingatcc-newfutureatcc-card-competitivecompensation-clk')]")
    __commitment_career_advancement = (By.XPATH, "//div[contains(@data-gtag-click-label,'cc-workingatcc-newfutureatcc-card-commitmenttocareeradvancement-clk')]")
    __employee_recognition = (By.XPATH, "//div[contains(@data-gtag-click-label,'cc-workingatcc-newfutureatcc-card-employeerecognition-clk')]")
    __flexible_work_from_home = (By.XPATH, "//div[contains(@data-gtag-click-label,'cc-workingatcc-newfutureatcc-card-flexibleworkfromhomeschedule-clk')]")
    __getting_time_destress = (By.XPATH, "//div[contains(@data-gtag-click-label,'cc-workingatcc-newfutureatcc-card-gettingtimetodestress-clk')]")


    __txt_training_education = (By.XPATH, "//p[contains(text(),'We provide opportunities for continued position-sp')]")
    __txt_competitive_compensation = (By.XPATH, "//p[contains(text(),'We value your education and past experience, but y')]")
    __txt_commitment_career_advancement = (By.XPATH, "//p[contains(text(),'Commitment pays. We reward staff members who commi')]")
    __txt_employee_recognition = (By.XPATH, "//p[contains(text(),'Our recognition program rewards team members who t')]")
    __txt_flexible_work_from_home = (By.XPATH, "//p[contains(text(),'We offer flexible work hours so you can plan your ')]")
    __txt_getting_time_destress = (By.XPATH, "//p[contains(text(),'We believe you should get time to destress and hav')]")

    __ivo_costa_img = (By.XPATH, "//img[contains(@title,'ivo-costa')]")
    __gina_parab_img = (By.XPATH, "//img[@title='gina-parab']")
    __snehal_naik_img = (By.XPATH, "//img[@title='snehal-naik']")

    __txt_snehal_naik =(By.CSS_SELECTOR, "div[class='carousel-item active'] div[class='member-level-2'] p")
    __txt_gina_parab = (By.XPATH, "//div[contains(@class,'carousel-item active')]//div[contains(@class,'member-level-2')]//p[1]")
    __txt_ivo_costa = (By.CSS_SELECTOR, "div[class='carousel-item active'] div[class='member-level-2'] p")


    __snehal_carousel_indicator = (By.XPATH, "//main[@class='container inner-page working-at-creative-capsule']//li[3]")
    __ivo_carousel_indicator = (By.XPATH, "//main[@class='container inner-page working-at-creative-capsule']//li[2]")
    __gina_carousel_indicator = (By.XPATH, "//main[@class='container inner-page working-at-creative-capsule']//li[1]")

    __next_arrow = (By.XPATH, "//a[@class='right carousel-control']//*[name()='svg']")
    __prev_arrow = (By.XPATH, "//a[@class='left carousel-control']//*[name()='svg']")

    __our_culture_img = (By.XPATH, "/html[1]/body[1]/main[1]/div[3]/section[5]/div[1]/div[1]/div[1]/div[1]/div[2]")
    __our_culture_img1 = (By.XPATH, "//div[@class='gallery-img img1-wrapper shadow-sm']//img")
    __our_culture_img2 = (By.XPATH, "//div[@class='gallery-img img2-wrapper shadow-sm']//img")
    __our_culture_img3 = (By.XPATH, "//div[@class='gallery-img img4-wrapper shadow-sm']//img")

    __followUs_link = (By.XPATH,"//a[@aria-label='LinkedIN']")
    __viewMore_link = (By.XPATH, "//a[normalize-space()='View more']")
    __viewOpenPositions_link = (By.XPATH, "//a[@data-gtag-category='WorkingAtCC-WeAreHiring']")
    __knowOurPeople_link = (By.XPATH, "//a[@data-gtag-category='WorkingAtCC-AllInOneTeam']")

    __CommonImage_inCompanyCulture = (By.XPATH, "//div[@class='grid-item featured']//img[@class='culture-image img-fluid cover']")
    __Close_inCompanyCulture = (By.XPATH, "//div[@class='close']//*[name()='svg']")
    __first_image_in_OurCulture = (By.XPATH, "//img[@class='img-fluid']")

    __linkedinSignIn = (By.XPATH, "//button[@class='authwall-join-form__form-toggle--bottom form-toggle']")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def open(self):
        self._driver.get(websiteUrl)

    def click_careers_menu(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__careers_menu))
        self._driver.find_element(*self.__careers_menu).click()


    def click_workingAtCC_menu(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__working_at_cc))
        self._driver.find_element(*self.__working_at_cc).click()

    def click_training_education(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__training_education))
        self._driver.find_element(*self.__training_education).click()


    def click_followus_link(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__followUs_link))
        self._driver.find_element(*self.__followUs_link).click()

    def click_viewMore_link(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__viewMore_link))
        self._driver.find_element(*self.__viewMore_link).click()

    def click_viewOpenPositions_link(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__viewOpenPositions_link))
        self._driver.find_element(*self.__viewOpenPositions_link).click()

    def click_knowOurPeople_link(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__knowOurPeople_link))
        self._driver.find_element(*self.__knowOurPeople_link).click()

    def click_ourCultureClose(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__Close_inCompanyCulture))
        self._driver.find_element(*self.__Close_inCompanyCulture).click()

    def click_commonImg(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__CommonImage_inCompanyCulture))
        self._driver.find_element(*self.__CommonImage_inCompanyCulture).click()

    def wait_till_firstImage_isDisplayed(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until(ec.presence_of_element_located(self.__first_image_in_OurCulture))
        the_first_image = self._driver.find_element(*self.__first_image_in_OurCulture)
        the_first_image.click()
        return the_first_image.is_displayed()


    def click_linkedIn_signIn(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__linkedinSignIn))
        self._driver.find_element(*self.__linkedinSignIn).click()


    def getTheBackPage(self):
        self._driver.back()

    @property
    def text_training_education(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_training_education))
        training_education_p = self._driver.find_element(*self.__txt_training_education)
        return training_education_p.text

    def click_competitive_compensation(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__competitive_compensation))
        self._driver.find_element(*self.__competitive_compensation).click()
    @property
    def text_competitive_compensation(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_competitive_compensation))
        return self._driver.find_element(*self.__txt_competitive_compensation).text

    def click_commitment_career_advancement(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__commitment_career_advancement))
        self._driver.find_element(*self.__commitment_career_advancement).click()
    @property
    def text_commitment_career_advancement(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_commitment_career_advancement))
        return self._driver.find_element(*self.__txt_commitment_career_advancement).text

    def click_employee_recognition(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__employee_recognition))
        self._driver.find_element(*self.__employee_recognition).click()
    @property
    def text_employee_recognition(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_employee_recognition))
        return self._driver.find_element(*self.__txt_employee_recognition).text

    def click_flexible_work_from_home(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__flexible_work_from_home))
        self._driver.find_element(*self.__flexible_work_from_home).click()

    @property
    def text_flexible_work_from_home(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_flexible_work_from_home))
        return self._driver.find_element(*self.__txt_flexible_work_from_home).text

    def click_getting_time_destress(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__getting_time_destress))
        self._driver.find_element(*self.__getting_time_destress).click()

    @property
    def text_getting_time_destress(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_getting_time_destress))
        return self._driver.find_element(*self.__txt_getting_time_destress).text


    def click_next_arrow(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__next_arrow))
        self._driver.find_element(*self.__next_arrow).click()

    def click_prev_arrow(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__prev_arrow))
        self._driver.find_element(*self.__prev_arrow).click()

    def click_gina_carouselIndicator(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__gina_carousel_indicator))
        self._driver.find_element(*self.__gina_carousel_indicator).click()

    def click_ivo_carouselIndicator(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__ivo_carousel_indicator))
        self._driver.find_element(*self.__ivo_carousel_indicator).click()

    def click_snehal_carouselIndicator(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__snehal_carousel_indicator))
        self._driver.find_element(*self.__snehal_carousel_indicator).click()

    @property
    def text_ivo_costa(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_ivo_costa))
        return self._driver.find_element(*self.__txt_ivo_costa).text
        # print(self._driver.find_element(*self.__txt_ivo_costa).text)

    @property
    def text_gina_parab(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_gina_parab))
        return self._driver.find_element(*self.__txt_gina_parab).text

    @property
    def text_snehal_naik(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__txt_snehal_naik))
        return self._driver.find_element(*self.__txt_snehal_naik).text

    def snehal_naik_image_isDisplayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__snehal_naik_img))
        return self._driver.find_element(*self.__snehal_naik_img).is_displayed()

    def gina_parab_image_isDisplayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__gina_parab_img))
        return self._driver.find_element(*self.__gina_parab_img).is_displayed()


    def ivo_costa_image_isDisplayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__ivo_costa_img))
        return self._driver.find_element(*self.__ivo_costa_img).is_displayed()


    def click_our_culture_img1(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__our_culture_img1))
        self._driver.find_element(*self.__our_culture_img1).click()
        self._driver.save_screenshot(ValueManager.save_screenshot_path_OurCultureImg1)

    def click_our_culture_img2(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__our_culture_img2))
        self._driver.find_element(*self.__our_culture_img2).click()
        self._driver.save_screenshot(ValueManager.save_screenshot_path_OurCultureImg2)

    @property
    def image_blur_css(self):
        return self._driver.find_element(*self.__our_culture_img).value_of_css_property("filter")
