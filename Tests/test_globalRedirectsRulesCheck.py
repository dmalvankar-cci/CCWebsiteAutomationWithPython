# Import packages

import pytest
from globalConstants import websiteUrl
from pageObjects.CCWebSearch_page import CCWebSearchPage


def test_globalRedirectsVerification(driver):

    """
        Need to verify the below redirects with the expected status codes
        Creativecapsule.com --> https://www.creativecapsule.com/
        www.creativecapsule.com --> https://www.creativecapsule.com/
        http://www.creativecapsule.com --> https://www.creativecapsule.com/
        http://creativecapsule.com --> https://www.creativecapsule.com/
        https://creativecapsule.com --> https://www.creativecapsule.com/
        Creativecapsule.com/ --> https://www.creativecapsule.com/
        CreativeCaPsuLe.com --> https://www.creativecapsule.com/
        CREATIVECAPSULE.COM --> https://www.creativecapsule.com/

        creativecapsul.us - https://www.creativecapsule.com/
        creativecapsule.us---https://www.creativecapsule.com/
        creativecapsul.com---https://www.creativecapsule.com/
        creativecapsule.ch--https://www.creativecapsule.com/de
        creativecapsule.net ---https://www.creativecapsule.com/
        creativecapsule.mobi---https://www.creativecapsule.com/

    """
    CCWebSearch_page = CCWebSearchPage(driver)





def test_bingSearchVerify(driver, check_browserSpecificTest):
    CCWebSearch_page = CCWebSearchPage(driver)
    # The entire testcase is in conftest.py file as it id browser specific testcase







def test_googleSearchVerify(driver):
    CCWebSearch_page = CCWebSearchPage(driver)
    CCWebSearch_page.googleSearch()
    assert CCWebSearch_page.current_url == websiteUrl, "Site Url is not matched"
    assert CCWebSearch_page.verifyIfCCLogoVisible(), "The CC logo isnt located"




def test_yahooSearchVerify(driver):
    CCWebSearch_page = CCWebSearchPage(driver)

    CCWebSearch_page.yahooSearch()

    driver.switch_to.window(driver.window_handles[1])
    assert CCWebSearch_page.current_url == websiteUrl, "Site Url is not matched"
    assert CCWebSearch_page.verifyIfCCLogoVisible(), "The CC logo isnt located"













