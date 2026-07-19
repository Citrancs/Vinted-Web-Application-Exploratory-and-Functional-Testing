from pages.general_page import GeneralPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage(GeneralPage):
    URL = "https://www.vinted.hu"

    def __init__(self, browser):
        # Meghívjuk a szülőosztály (GeneralPage) konstruktorát
        super().__init__(browser)

    def load(self):
        """Megnyitja a Vinted főoldalát a böngészőben."""
        self.open_webpage(self.URL)

    def login_registration_button(self):
        a_sign_in = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//a[@data-testid="header--login-button"]')))
        return a_sign_in

    def cookies_accept_button(self):
        button_accept = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.ID,"onetrust-accept-btn-handler")))
        return button_accept

    def accept_cookies(self):
        self.cookies_accept_button().click()
        # Megvárjuk, amíg a takaró süti banner teljesen ELTŰNIK a képernyőről!
        WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "ot-dpd-container"))
        )

    def click_login_button(self):
        self.login_registration_button().click()

    def input_search_bar(self, product_name):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.ID,"search_text"))).send_keys(product_name)

    def select_suggestion_by_index(self, index=0):
        # 1. Megvárjuk, amíg a javaslatok listája megjelenik a DOM-ban és láthatóvá válik
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="item-suggestions"]'))
        )

        # 2. Összegyűjtjük az összes javaslat elemet egy listába
        suggestions = self.browser.find_elements(By.CSS_SELECTOR, '[data-testid="search-suggestion-bg"]')

        # 3. Rákattintunk a kért indexű elemre (alapértelmezetten a 0.-ra)
        suggestions[index].click()
