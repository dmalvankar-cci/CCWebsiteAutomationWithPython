# Import packages
import pytest

from globalConstants import websiteUrl
from pageObjects.globalRedirectsRule_page import globalRedirectsRulePage


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
    globalRedirectsRule_page = globalRedirectsRulePage(driver)




def test_bingSearchVerify(driver):
    globalRedirectsRule_page = globalRedirectsRulePage(driver)

    globalRedirectsRule_page.bingSearch()
    # globalRedirectsRule_page.bingCCLinkClick()
    driver.switch_to.window(driver.window_handles[1])
    assert globalRedirectsRule_page.current_url == websiteUrl, "Site Url is not matched"

def test_googleSearchVerify(driver):
    globalRedirectsRule_page = globalRedirectsRulePage(driver)
    globalRedirectsRule_page.googleSearch()
    # driver.switch_to.window(driver.window_handles[2])
    assert globalRedirectsRule_page.current_url == websiteUrl, "Site Url is not matched"

    # globalRedirectsRule_page.yahooSearch()

def test_yahooSearchVerify(driver):
    globalRedirectsRule_page = globalRedirectsRulePage(driver)

    globalRedirectsRule_page.yahooSearch()
    # globalRedirectsRule_page.bingCCLinkClick()
    driver.switch_to.window(driver.window_handles[1])
    assert globalRedirectsRule_page.current_url == websiteUrl, "Site Url is not matched"










