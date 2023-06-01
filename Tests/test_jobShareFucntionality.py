import time

import readExcelData
from ValueManager import sharedPost
from pageObjects.CCJobShare_page import CCJobSharePage


def test_checkJobShareLinkedin(driver):


    CCJobShare_page = CCJobSharePage(driver)

    # Take username and password from Excel sheet
    username = readExcelData.read_data(2, 1)
    password = readExcelData.read_data(2, 2)

    # open positions page
    CCJobShare_page.open()
    # Open any post
    CCJobShare_page.clickPost()
    # Click on LinkedIn share icon
    CCJobShare_page.clickLinkedInShare()
    # In the LinkedIn window perform login
    driver.switch_to.window(driver.window_handles[1])
    CCJobShare_page.perform_login(username, password)
    # Click on share post
    CCJobShare_page.postToLinkedIn()
    # Verify if the OG image is shown
    assert CCJobShare_page.linkedPostImg_isDisplayed(), "The image isnt displayed"
    # Continue the share till the post gets shared
    CCJobShare_page.afterOTGVerification()
    # Take screenshot once the post is shared
    # Click on the shared post
    driver.switch_to.window(driver.window_handles[2])
    CCJobShare_page.linkedinAfterSharing()
    # Verify if the post Url is matches to the shared one
    assert CCJobShare_page.current_url == sharedPost, "The url is not matched to shared one"





