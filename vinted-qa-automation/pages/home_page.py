from pages.general_page import GeneralPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class HomePage(GeneralPage):
    URL = "https://www.vinted.hu"

    def __init__(self, browser):
        # Meghívjuk a szülőosztály (GeneralPage) konstruktorát
        super().__init__(browser)

    def load(self):
        """Megnyitja a Vinted főoldalát a böngészőben."""
        self.open_webpage(self.URL)

    def login_registration_button(self):
        a_sign_in = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="header--login-button"]')))
        return a_sign_in

    def cookies_accept_button(self):
        button_accept = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
        return button_accept

    def accept_cookies(self):
        self.cookies_accept_button().click()

    def click_login_button(self):
        self.login_registration_button().click()