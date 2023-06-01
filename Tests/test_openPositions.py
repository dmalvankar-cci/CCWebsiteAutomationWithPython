import time
import pytest
import ValueManager
from pageObjects import WorkingAtCC_page
from pageObjects.OpenPositions_page import OpenPositionsPage

from pageObjects.WorkingAtCC_page import WorkingAtCCPage


@pytest.fixture
def test_verifyIFWorkingAtCC_isOpened(driver):
    """
      Test : Verify if the "Open positions" page is opened
      Validate the page URl
      URL : https://www.creativecapsule.com/open-positions/
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    OpenPositions_page = OpenPositionsPage(driver)
    # Open the site
    WorkingAtCC_page.open()
    # Click on the "careers" menu
    WorkingAtCC_page.click_careers_menu()
    # Click on the "open positions" menu
    OpenPositions_page.click_openPositions_menu()
    # Verify the url
    assert WorkingAtCC_page.current_url == ValueManager.openPositionUrl

def test_invalidSearchFunctionality(driver, test_verifyIFWorkingAtCC_isOpened):
    """
           Test : Verify the Invalid search
           URL : https://www.creativecapsule.com/open-positions/
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    OpenPositions_page = OpenPositionsPage(driver)
    # enter text as "tttt" in the search field
    OpenPositions_page.invalidSearch()
    # verify the result for invalid text
    assert OpenPositions_page.verify_invalidSearchTxt == ValueManager.invalidSearchedText, "Text is not matching"
    # click on the application link
    OpenPositions_page.click_applicationLink()
    # verify if the correct page is opened
    assert WorkingAtCC_page.current_url == ValueManager.genericPositionUrl

def test_verifyClose_inTheSearchField(driver, test_verifyIFWorkingAtCC_isOpened):
    """
              Test : Verify the close icon and the placeholder
              URL : https://www.creativecapsule.com/open-positions/
    """

    OpenPositions_page = OpenPositionsPage(driver)
    # verify the placeholder text
    assert OpenPositions_page.get_textFromSearchField == ValueManager.placeholder, "Text is not matching"
    # enter text as "tttt" in the search field
    OpenPositions_page.invalidSearch()
    # verify the result for invalid text
    assert OpenPositions_page.verify_invalidSearchTxt == ValueManager.invalidSearchedText, "Text is not matching"
    # click on the close icon
    OpenPositions_page.click_searchClose()
    # verify if the placeholder text is shown
    assert OpenPositions_page.get_textFromSearchField == ValueManager.placeholder, "Text is not matching"

def test_validSearchFunctionality(driver, test_verifyIFWorkingAtCC_isOpened):
    """
          Test : Verify the search functionality for valid text
          Validate the searched result
          URL : https://www.creativecapsule.com/open-positions/
    """

    WorkingAtCC_page = WorkingAtCCPage(driver)
    OpenPositions_page = OpenPositionsPage(driver)
    # enter text as ".net developer" in the search field
    OpenPositions_page.validSearch()
    # verify if the dot net position is shown
    assert OpenPositions_page.verify_dotNetTxt == ValueManager.validTextToPassInTheSearchField, "Text is not matching"
    # click on the dot net position
    OpenPositions_page.click_dotNet()
    # verify if the .net position is opened
    assert WorkingAtCC_page.current_url == ValueManager.dotNetDevUrl
@pytest.mark.testme
def test_applyHereLink(driver, test_verifyIFWorkingAtCC_isOpened):
    """
             Test : Verify if the apply here link is opening the generic position
             URL : https://www.creativecapsule.com/open-positions/
    """

    WorkingAtCC_page = WorkingAtCCPage(driver)
    OpenPositions_page = OpenPositionsPage(driver)
    # click on the apply here link
    OpenPositions_page.click_applyHere_link()
    # verify if the correct page is opened
    assert WorkingAtCC_page.current_url == ValueManager.genericPositionUrl