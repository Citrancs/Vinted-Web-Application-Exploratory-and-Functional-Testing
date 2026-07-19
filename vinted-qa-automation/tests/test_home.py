import pytest
import allure
import urllib.parse
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


@allure.title("TC03 - Search product without login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Positive", "Smoke", "Navigation", "Homepage", "Guest")
@pytest.mark.parametrize(
    ("product_name", "description"),
    [
        ("póló", "Testing search product without login")
    ])
def test_searching_product(browser, product_name, description):
    home_page = HomePage(browser)
    home_page.load()
    home_page.accept_cookies()
    home_page.input_search_bar(product_name)
    home_page.select_suggestion_by_index(0)
    # 1. Lekérjük az aktuális URL-t a böngészőtől
    actual_url = browser.current_url
    # 2. Dekódoljuk az URL-t (hogy a %C3%B3-ból újra 'ó' legyen)
    decoded_url = urllib.parse.unquote(actual_url)
    # 3. Az ASSERT: megnézzük, hogy a "póló" kulcsszó benne van-e a tiszta URL-ben
    assert "póló" in decoded_url, f"Hiba! A 'póló' szó nem található az URL-ben. Az aktuális URL: {decoded_url}"
