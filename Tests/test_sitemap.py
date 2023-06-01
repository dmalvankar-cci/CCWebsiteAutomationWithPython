import pytest
import ValueManager
from pageObjects import WorkingAtCC_page
from pageObjects.OpenPositions_page import OpenPositionsPage
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
    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    assert Sitemap_page.verify_PageSitemapText == ValueManager.pageSitemapTxt, "Text is not matching"
    assert Sitemap_page.table_rows_count == 37, "The row count is not matching"
    assert Sitemap_page.verify_someOfLinks == ValueManager.sitemapLinksGroup, "Group links are not matching"

def test_verifySomeRandomLinks(driver, test_verifyTheSitemaps):
    WorkingAtCC_page = WorkingAtCCPage(driver)
    Sitemap_page = SitemapPage(driver)
    # Sitemap_page.click_deNews()
    # assert WorkingAtCC_page.current_url == ValueManager.deNewsUrl, "The url is not matching"
    # WorkingAtCC_page.getTheBackPage()
    Sitemap_page.click_enOurLeadership()
    assert WorkingAtCC_page.current_url == ValueManager.ourLeadershipUrl, "The url is not matching"
    WorkingAtCC_page.getTheBackPage()
    # Sitemap_page.click_deSpc()
    # assert WorkingAtCC_page.current_url == ValueManager.deSpcUrl, "The url is not matching"
    # WorkingAtCC_page.getTheBackPage()
    Sitemap_page.click_enSpc()
    assert WorkingAtCC_page.current_url == ValueManager.spcUrl, "The url is not matching"
    WorkingAtCC_page.getTheBackPage()
    Sitemap_page.click_enOpenPositions()
    assert WorkingAtCC_page.current_url == ValueManager.openPositionUrl, "The url is not matching"





