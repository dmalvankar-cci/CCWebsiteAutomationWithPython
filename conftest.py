import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from ValueManager import websiteUrl
from pageObjects.CCWebSearch_page import CCWebSearchPage


#Open browser
@pytest.fixture
# @pytest.fixture(params=["chrome","firefox","edge"])
def driver(request):
    browser=request.config.getoption("--browser")
    # browser=request.param
    print(f'Creating Driver for {browser} Broswer')

    # Open Browser
    if browser == "chrome":
        browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        browser_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        browser_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f"Expected browser to be chrome, edge, firefox. got {browser}")
    browser_driver.maximize_window()
    yield browser_driver
    print(f'Closing Driver for {browser} Browser')
    browser_driver.quit()



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="Provide browser as chrome, Edge or firefox")

# @pytest.fixture(params=["chrome","firefox","edge"])
@pytest.fixture
def check_browserSpecificTest(driver, request):
    # browser = request.param
    browser = request.config.getoption("--browser")
    CCWebSearch_page = CCWebSearchPage(driver)


    if browser == "firefox" "Edge":
        CCWebSearch_page.bingSearch()
        driver.switch_to.window(driver.window_handles[1])
        assert CCWebSearch_page.current_url == websiteUrl, "Site Url is not matched"
        assert CCWebSearch_page.verifyIfCCLogoVisible(), "The CC logo isnt located"

    elif browser == "chrome":
        CCWebSearch_page.bingSearch()
        assert CCWebSearch_page.current_url == websiteUrl, "Site Url is not matched"
        assert CCWebSearch_page.verifyIfCCLogoVisible(), "The CC logo isnt located"






