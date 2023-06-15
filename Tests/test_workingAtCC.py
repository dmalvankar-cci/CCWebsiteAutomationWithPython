import time

import pytest

import ValueManager
import readExcelData
from ValueManager import workingAtCCUrl
from pageObjects.JobDescriptions_page import JobDescriptionsPage
from pageObjects.WorkingAtCC_page import WorkingAtCCPage

@pytest.fixture
def test_verifyIFWorkingAtCC_isOpened(driver):
    """
      Test : Verify if the "Working at CC" page is opened
      Validate the page URl
      URL : https://www.creativecapsule.com/working-at-creative-capsule/
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    # Open the site
    WorkingAtCC_page.open()
    # Click on the "careers" menu
    WorkingAtCC_page.click_careers_menu()
    # Click on the "working at cc" menu
    WorkingAtCC_page.click_workingAtCC_menu()
    # Verify the url
    assert WorkingAtCC_page.current_url == workingAtCCUrl

def test_verify_tabs(driver, test_verifyIFWorkingAtCC_isOpened):
    """
         Test : Validate if the expected tab is opened
         URL : https://www.creativecapsule.com/working-at-creative-capsule/
    """

    WorkingAtCC_page = WorkingAtCCPage(driver)
    # Click on the "Getting time destress" tab
    WorkingAtCC_page.click_getting_time_destress()
    # Verify the if the "Getting time destress" tab is opened
    assert WorkingAtCC_page.text_getting_time_destress == ValueManager.getting_time_destress, "The text is not matching"

    # Click on the "Flexible work from home" tab
    WorkingAtCC_page.click_flexible_work_from_home()
    # Verify the if the "Flexible work from home" tab is opened
    assert WorkingAtCC_page.text_flexible_work_from_home == ValueManager.flexible_work_from_home, "The text is not matching"

    # Click on the "Employee Recognition" tab
    WorkingAtCC_page.click_employee_recognition()
    # Verify the if the "Employee Recognition" tab is opened
    assert WorkingAtCC_page.text_employee_recognition == ValueManager.employee_recognition, "The text is not matching"

    # Click on the "Training Education" tab
    WorkingAtCC_page.click_training_education()
    # Verify the if the "Training Education" tab is opened
    assert WorkingAtCC_page.text_training_education == ValueManager.training_education, "The text is not matching"

    # Click on the "Competitive Compensation" tab
    WorkingAtCC_page.click_competitive_compensation()
    # Verify the if the "Competitive Compensation" tab is opened
    assert WorkingAtCC_page.text_competitive_compensation == ValueManager.competitive_compensation, "The text is not matching"

    # Click on the "Commitment career advancement" tab
    WorkingAtCC_page.click_commitment_career_advancement()
    # Verify the if the "Commitment career advancement" tab is opened
    assert WorkingAtCC_page.text_commitment_career_advancement == ValueManager.commitment_career_advancement, "The text is not matching"


def test_verify_testimonial(driver, test_verifyIFWorkingAtCC_isOpened):
    """
            Test : Validate the testimonial section, verify if the expected member's info is shown onclick of the Carousel indicator
            URL : https://www.creativecapsule.com/working-at-creative-capsule/
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    # WorkingAtCC_page.click_gina_carouselIndicator()
    # Verify if the Gina Parab text is shown
    assert WorkingAtCC_page.text_gina_parab == ValueManager.gina_parab_text, "Text is not matching"
    # Verify if the Gina Parab image is shown
    assert WorkingAtCC_page.gina_parab_image_isDisplayed() == True, "The gina's image is not there"

    # Click on the middle carousel indicator
    WorkingAtCC_page.click_ivo_carouselIndicator()
    # Verify if the Ivo Costa text is shown
    assert WorkingAtCC_page.text_ivo_costa == ValueManager.ivo_costa_text, "Text is not matching"
    # Verify if the Ivo Costa image is shown
    assert WorkingAtCC_page.ivo_costa_image_isDisplayed() == True, "The ivo's image is not there"

    # Click on the last carousel indicator
    WorkingAtCC_page.click_snehal_carouselIndicator()
    # Verify if the Snehal Naik text is shown
    assert WorkingAtCC_page.text_snehal_naik == ValueManager.snehal_naik_text, "Text is not matching"
    # Verify if the Snehal Naik  image is shown
    assert WorkingAtCC_page.snehal_naik_image_isDisplayed() == True, "The snehal's image is not there"

    # Click on the next arrow
    WorkingAtCC_page.click_next_arrow()
    # Verify if the Gina Parab text is shown
    assert WorkingAtCC_page.gina_parab_image_isDisplayed() == True, "The gina's image is not there"

    # Click on the previous arrow
    WorkingAtCC_page.click_prev_arrow()
    # Verify if the Snehal Naik  image is shown
    assert WorkingAtCC_page.snehal_naik_image_isDisplayed() == True, "The snehal's image is not there"



def test_ourCulture(driver, test_verifyIFWorkingAtCC_isOpened):
    """
            Test : Verify the hover effect for "Our Culture images"
            URL : https://www.creativecapsule.com/working-at-creative-capsule/
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    # Click on the images
    WorkingAtCC_page.click_our_culture_img1()
    WorkingAtCC_page.click_our_culture_img2()
    # Verify the CSS property the blur effect
    assert WorkingAtCC_page.image_blur_css == "grayscale(0)", "The css value didnt matched"


@pytest.mark.testme
def test_linksNavigation(driver, test_verifyIFWorkingAtCC_isOpened):
    """
            Test : Verify the links from the page are redirecting to the correct pages
            URL : https://www.creativecapsule.com/working-at-creative-capsule/
    """

    # Take username and password from Excel sheet
    username = readExcelData.read_data(2, 1)
    password = readExcelData.read_data(2, 2)
    JobDescriptions_page = JobDescriptionsPage(driver)
    WorkingAtCC_page = WorkingAtCCPage(driver)

    # get back to the "working at cc page"
    driver.switch_to.window(driver.window_handles[0])
    # Click on the "know our people" link
    WorkingAtCC_page.click_knowOurPeople_link()
    # Verify if the "our people" page is opened
    assert WorkingAtCC_page.current_url == ValueManager.ourPeopleUrl
    # get back to the "working at cc page"
    WorkingAtCC_page.getTheBackPage()
    # Click on the "view more" link
    WorkingAtCC_page.click_viewMore_link()
    # Verify if the "company culture" page is opened
    assert WorkingAtCC_page.current_url == ValueManager.companyCultureUrl
    # Click on the first image
    WorkingAtCC_page.click_commonImg()
    # verify if the first image is opened
    assert WorkingAtCC_page.wait_till_firstImage_isDisplayed
    # Click on the close
    WorkingAtCC_page.click_ourCultureClose()
    # get back to the "working at cc page"
    WorkingAtCC_page.getTheBackPage()
    # Click on the "view open positions" link
    WorkingAtCC_page.click_viewOpenPositions_link()
    # Verify if the "open positions" page is opened
    assert WorkingAtCC_page.current_url == ValueManager.openPositionUrl
    # get back to the "working at cc page"
    WorkingAtCC_page.getTheBackPage()
    # Click on the "follow us" link
    WorkingAtCC_page.click_followus_link()
    # Verify if the "linkedin" page is opened
    driver.switch_to.window(driver.window_handles[1])
    WorkingAtCC_page.click_linkedIn_signIn()
    JobDescriptions_page.perform_login(username, password)
    driver.switch_to.window(driver.window_handles[0])
    WorkingAtCC_page.click_followus_link()
    driver.switch_to.window(driver.window_handles[2])
    assert WorkingAtCC_page.current_url == ValueManager.CClinkedInPageUrl


















