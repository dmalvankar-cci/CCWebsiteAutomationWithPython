import time

import pytest

import ValueManager
import readExcelData
from ValueManager import sharedPost
from pageObjects.JobDescriptions_page import JobDescriptionsPage
from pageObjects.WorkingAtCC_page import WorkingAtCCPage


def test_checkJobShareLinkedin(driver):


    JobDescriptions_page = JobDescriptionsPage(driver)
    WorkingAtCC_page = WorkingAtCCPage(driver)

    # Take username and password from Excel sheet
    username = readExcelData.read_data(2, 1)
    password = readExcelData.read_data(2, 2)

    # open positions page
    JobDescriptions_page.open()
    # Open any post
    JobDescriptions_page.clickPost()
    # Click on LinkedIn share icon
    JobDescriptions_page.clickLinkedInShare()
    # In the LinkedIn window perform login
    driver.switch_to.window(driver.window_handles[1])
    # WorkingAtCC_page.click_linkedIn_signIn()
    JobDescriptions_page.perform_login(username, password)
    # Click on share post
    JobDescriptions_page.postToLinkedIn()
    # Verify if the OG image is shown
    assert JobDescriptions_page.linkedPostImg_isDisplayed(), "The image isnt displayed"
    # Continue the share till the post gets shared
    JobDescriptions_page.afterOTGVerification()
    # Take screenshot once the post is shared
    # Click on the shared post
    driver.switch_to.window(driver.window_handles[2])
    JobDescriptions_page.linkedinAfterSharing()
    # Verify if the post Url is matches to the shared one
    assert JobDescriptions_page.current_url == sharedPost, "The url is not matched to shared one"


def test_FbSharing(driver):
    JobDescriptions_page = JobDescriptionsPage(driver)
    WorkingAtCC_page = WorkingAtCCPage(driver)

    # Take username and password from Excel sheet
    username = readExcelData.read_data(3, 1)
    password = readExcelData.read_data(3, 2)

    # open positions page
    JobDescriptions_page.open()
    # Open any post
    JobDescriptions_page.clickPost()
    # Click on Facebook share icon
    JobDescriptions_page.click_FBShare()
    # In the LinkedIn window perform login
    driver.switch_to.window(driver.window_handles[1])
    JobDescriptions_page.perform_login_fb(username, password)
    # Select facebook friend
    JobDescriptions_page.select_fb_friend()
    # send post to facebook
    JobDescriptions_page.click_send_fbPost()

@pytest.mark.testme
def test_verifyCopyLink(driver):
    JobDescriptions_page = JobDescriptionsPage(driver)
    # open positions page
    JobDescriptions_page.open()
    #  Open any post
    JobDescriptions_page.clickPost()
    # Click on Facebook share icon
    JobDescriptions_page.click_copyLink()
    JobDescriptions_page.pasteLink()
    # Verify if the opened Url is matches to the copied one
    assert JobDescriptions_page.getTextFromSearch == sharedPost, "The url is not matched to copied one"


def test_linksNavigation(driver):
    JobDescriptions_page = JobDescriptionsPage(driver)
    # open positions page
    JobDescriptions_page.open()
    #  Open any post
    JobDescriptions_page.clickPost()
    # click apply online link
    JobDescriptions_page.click_applyOnline_link()
    # verify if the link is redirecting to dot net developer apply online form
    assert JobDescriptions_page.current_url == ValueManager.dotNetFormUrl, "The url is not matched"
    # visit the back to the Job description page
    driver.back()
    # click open positions link
    JobDescriptions_page.click_openPositions_link()
    # verify if the link is redirecting to the open position page
    assert JobDescriptions_page.current_url == ValueManager.openPositionUrl, "The url is not matched"
    # visit the back to the Job description page
    driver.back()
    # click about us link
    JobDescriptions_page.click_aboutUs_link()
    # verify if the link is redirecting to the about us page
    assert JobDescriptions_page.current_url == ValueManager.aboutUsUrl, "The url is not matched"
    # visit the back to the Job description page
    driver.back()
    # click working at creative capsule link
    JobDescriptions_page.click_workingAtCC_link()
    # verify if the link is redirecting to the working at creative capsule page
    assert JobDescriptions_page.current_url == ValueManager.workingAtCCUrl, "The url is not matched"
    # visit the back to the Job description page
    driver.back()
    # click career path link
    JobDescriptions_page.click_careerPath_link()
    # verify if the link is redirecting to the career path page
    assert JobDescriptions_page.current_url == ValueManager.careerPathUrl, "The url is not matched"
    # visit the back to the Job description page
    driver.back()


def test_verifyWhatsappShare(driver):
    JobDescriptions_page = JobDescriptionsPage(driver)
    # open positions page
    JobDescriptions_page.open()
    #  Open any post
    JobDescriptions_page.clickPost()
    JobDescriptions_page.click_whatsapp_share()
    time.sleep(15)


def test_verifyPositionNumbers(driver):
    JobDescriptions_page = JobDescriptionsPage(driver)
    # open positions page
    JobDescriptions_page.open()
    #  Open any post
    JobDescriptions_page.clickPost()
    assert JobDescriptions_page.positionNumbersVerification == ValueManager.JobDesciptionPage_PositionNumbers, "The position number is not matched"