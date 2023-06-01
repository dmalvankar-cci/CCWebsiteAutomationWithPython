import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import ValueManager

class SitemapPage:

    __text_for_sitemaps = (By.XPATH, "//p[normalize-space()='This XML Sitemap Index file contains 1 sitemaps.']")
    __text_for_pageSitemap = (By.XPATH, "//p[normalize-space()='This XML Sitemap contains 37 URLs.']")
    __table_rows = (By.XPATH, "//tbody//tr")
    __table_cols = (By.XPATH, "//*[@id= 'sitemap']/thead/tr/th")
    __page_sitemap = (By.LINK_TEXT, "https://www.creativecapsule.com/page-sitemap.xml")

    __de_news = (By.LINK_TEXT, "https://www.creativecapsule.com/de/news/")
    __en_our_leadership = (By.LINK_TEXT, "https://www.creativecapsule.com/our-leadership/")
    __en_spc = (By.LINK_TEXT, "https://www.creativecapsule.com/software-companies/")
    __de_spc = (By.LINK_TEXT, "https://www.creativecapsule.com/de/software-companies/")
    __en_openPositions = (By.LINK_TEXT, "https://www.creativecapsule.com/open-positions/")

    __sitemap = (By.XPATH, "//tbody//tr//td[1]")
    def open(self):
        self._driver.get(ValueManager.sitemapUrl)


    def __init__(self,driver:WebDriver):
        self._driver = driver

    @property
    def table_rows_count(self):
        return len(self._driver.find_elements(*self.__table_rows))

    def click_sitemap(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__sitemap))
        self._driver.find_element(*self.__sitemap).click()

    @property
    def verify_someOfLinks(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__de_news))
        deNews = self._driver.find_element(*self.__de_news)
        enOurLeadership = self._driver.find_element(*self.__en_our_leadership)
        enSpc = self._driver.find_element(*self.__en_spc)
        deSpc = self._driver.find_element(*self.__de_spc)
        return deNews.text, enOurLeadership.text, enSpc.text, deSpc.text

    @property
    def verify_pageSitemapLinkTxt(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__page_sitemap))
        pageSitemap = self._driver.find_element(*self.__page_sitemap)
        return pageSitemap.text

    @property
    def verify_SitemapText(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__text_for_sitemaps))
        SitemapTxt = self._driver.find_element(*self.__text_for_sitemaps)
        return SitemapTxt.text

    @property
    def verify_PageSitemapText(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__text_for_pageSitemap))
        SitemapTxt = self._driver.find_element(*self.__text_for_pageSitemap)
        return SitemapTxt.text

    def click_deNews(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__de_news))
        self._driver.find_element(*self.__de_news).click()

    def click_enOurLeadership(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__en_our_leadership))
        self._driver.find_element(*self.__en_our_leadership).click()

    def click_enSpc(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__en_spc))
        self._driver.find_element(*self.__en_spc).click()

    def click_deSpc(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__de_spc))
        self._driver.find_element(*self.__de_spc).click()

    def click_enOpenPositions(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__en_openPositions))
        self._driver.find_element(*self.__en_openPositions).click()


