import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage


@allure.title("TC01 - Login with e-mail and password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Positive", "Functional", "Login")
@pytest.mark.parametrize(
    "email, password, description",
    [
        ("test3@test.hu", "1234_Abcd", "Login with e-mail and password")
    ])
def test_login_happy_path(browser, email, password, description):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    # Betölti a login oldalt
    login_page.load()
    home_page.accept_cookies()
    # Rákattintunk a "Bejelentkezés" gombra
    login_page.login_button_click()
    login_page.login_with_email_button_click()
    login_page.input_username_or_email(email)
    login_page.input_password(password)
    login_page.button_submit_click()
