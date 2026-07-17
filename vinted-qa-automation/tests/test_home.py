from pages.home_page import HomePage

def test_vinted_homepage_loads(browser):
    # 1. Példányosítjuk a HomePage-et, és átadjuk neki a 'browser' fixture-t
    home_page = HomePage(browser)

    # 2. Betöltjük az oldalt
    home_page.load()

    # 3. Ellenőrizzük (assert), hogy jó helyen járunk-e
    # Megnézzük, hogy a Vinted szó benne van-e az oldal címében (Title)
    assert "Vinted" in home_page.get_title(), "A Vinted főoldal nem töltődött be megfelelően!"