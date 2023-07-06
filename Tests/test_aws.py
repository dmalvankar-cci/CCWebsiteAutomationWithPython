import time

import pytest

from pageObjects.AWS_page import AWSPage



def test_clientSlider(driver):


    AWS_page = AWSPage(driver)
    AWS_page.open()
    AWS_page.scollToSlider()
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_leftArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_rightArrow()
    time.sleep(2)
    AWS_page.check_presence()

    AWS_page.click_rightArrow()
    time.sleep(2)
    AWS_page.check_presence()

