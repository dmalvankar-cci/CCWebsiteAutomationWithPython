import pytest
import ValueManager
from pageObjects.Sitemap_page import SitemapPage

from pageObjects.WorkingAtCC_page import WorkingAtCCPage
@pytest.fixture
def test_verifyIFSitemap_isOpened(driver):
    """
          Test : Verify if the "Sitemap" page is opened
          Validate the page URl
          URL : https://www.creativecapsule.com/sitemap_index.xml
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    # Open the sitemap page
    Sitemap_page.open()
    # Verify the url
    assert WorkingAtCC_page.current_url == ValueManager.sitemapUrl


@pytest.fixture
def test_verifyTheSitemaps(driver, test_verifyIFSitemap_isOpened):
    """
              Test : Verify if the only one sitemap is present as
              URL : https://www.creativecapsule.com/sitemap_index.xml
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    assert Sitemap_page.verify_pageSitemapLinkTxt == ValueManager.pageSitemapUrl, "Text is not matching"
    assert Sitemap_page.verify_SitemapText == ValueManager.sitemapTxt, "text is not matching"
    assert Sitemap_page.table_rows_count == 1, "The row count is not matching"
    Sitemap_page.click_sitemap()
    assert WorkingAtCC_page.current_url == ValueManager.pageSitemapUrl, "The url is not matching"



def test_verifyThePageSitemap(driver, test_verifyTheSitemaps):
    """
            Test : Verify if the all 37 rows are present in the table
            and verify some random links if those are present
            URL : https://www.creativecapsule.com/page-sitemap.xml
    """

    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    # verify the text on the page sitemap
    assert Sitemap_page.verify_PageSitemapText == ValueManager.pageSitemapTxt, "Text is not matching"
    # verify the row count is 37
    assert Sitemap_page.table_rows_count == 37, "The row count is not matching"
    # verify some random links text
    assert Sitemap_page.verify_someOfLinks == ValueManager.sitemapLinksGroup, "Group links are not matching"

def test_verifySomeRandomLinks(driver, test_verifyTheSitemaps):
    """
        Test : Verify the navigation of some links
        URL : https://www.creativecapsule.com/page-sitemap.xml
    """
    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    # Click our leadership link
    Sitemap_page.click_enOurLeadership()
    # verify redirection of the leadership link
    assert WorkingAtCC_page.current_url == ValueManager.ourLeadershipUrl, "The url is not matching"
    WorkingAtCC_page.getTheBackPage()
    # Click spc page link
    Sitemap_page.click_enSpc()
    # verify redirection of the spc link
    assert WorkingAtCC_page.current_url == ValueManager.spcUrl, "The url is not matching"
    WorkingAtCC_page.getTheBackPage()
    # click open positions link
    Sitemap_page.click_enOpenPositions()
    # verify redirection of the open positions link
    assert WorkingAtCC_page.current_url == ValueManager.openPositionUrl, "The url is not matching"





