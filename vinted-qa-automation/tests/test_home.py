import pytest
import allure
from pages.home_page import HomePage


@allure.title("TC01 - Home page load")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Positive", "Smoke", "Homepage")
@pytest.mark.parametrize(
    "description",
    [
        "Home page load"
    ])
def test_vinted_homepage_loads(browser, description):
    # 1. Példányosítjuk a HomePage-et, és átadjuk neki a 'browser' fixture-t
    home_page = HomePage(browser)

    # 2. Betöltjük az oldalt
    home_page.load()

    # 3. Ellenőrizzük (assert), hogy jó helyen járunk-e
    # Megnézzük, hogy a Vinted szó benne van-e az oldal címében (Title)
    assert "Vinted" in home_page.get_title(), "A Vinted főoldal nem töltődött be megfelelően!"


@allure.title("TC02 - Navigate to login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Positive", "Smoke", "Navigation", "Homepage")
@pytest.mark.parametrize(
    "description",
    [
        "Navigate to login"
    ])
def test_navigate_to_login_page(browser, description):
    home_page = HomePage(browser)
    home_page.load()
    home_page.accept_cookies()
    home_page.click_login_button()

    # ELLENŐRZÉS (Assert): Megnézzük, hogy az URL-ben szerepel-e a regisztrációs/bejelentkezési rész
    assert "signup" in home_page.get_current_url(), "Nem sikerült átnavigálni a bejelentkező oldalra!"
