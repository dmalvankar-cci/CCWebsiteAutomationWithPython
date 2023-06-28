import time

import pytest

import ValueManager
from pageObjects.ApplyOnline_page import ApplyOnlinePage



def test_EmptyFormValidation(driver):

    ApplyOnline_page = ApplyOnlinePage(driver)
    ApplyOnline_page.open()
    ApplyOnline_page.click_nextBtn()
    assert ApplyOnline_page.error_GlobalTxt == ValueManager.GlobalErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_FnameTxt == ValueManager.FnameErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_LnameTxt == ValueManager.LnameErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_EmailTxt == ValueManager.EmailErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_DOBTxt == ValueManager.DOBErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_EducationTxt == ValueManager.EducationErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_PhoneTxt == ValueManager.PhoneErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_CVTxt == ValueManager.ResumeErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_CoverletterTxt == ValueManager.CoverletterErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_CityTxt == ValueManager.CityErrorTxt, "The error text is not matching"
    assert ApplyOnline_page.error_StateTxt == ValueManager.StateErrorTxt, "The error text is not matching"
    ApplyOnline_page.click_radioBtn()
    ApplyOnline_page.click_nextBtn()
    assert ApplyOnline_page.error_CCEmployeeTxt == ValueManager.CCEmployeeErrorTxt, "The error text is not matching"
