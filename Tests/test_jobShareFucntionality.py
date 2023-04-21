import time

import readExcelData
from pageObjects.CCJobShare_page import CCJobSharePage


def test_checkJobShare(driver):


    CCJobShare_page = CCJobSharePage(driver)

    username = readExcelData.read_data(2, 1)
    password = readExcelData.read_data(2, 2)

    CCJobShare_page.open()
    CCJobShare_page.clickPost()
    CCJobShare_page.clickLinkedInShare()
    driver.switch_to.window(driver.window_handles[1])
    CCJobShare_page.perform_login(username, password)
    CCJobShare_page.postToLinkedIn()
    assert CCJobShare_page.linkedPostImg_isDisplayed(), "The image isnt displayed"
    CCJobShare_page.afterOTGVerification()
    CCJobShare_page.linkedinAfterSharing()




