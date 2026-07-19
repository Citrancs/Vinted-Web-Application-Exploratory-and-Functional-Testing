from selenium.webdriver.remote.webelement import WebElement

from pages.general_page import GeneralPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(GeneralPage):
    URL = "https://www.vinted.hu/member/signup/select_type?ref_url=%2F"

    def __init__(self, browser):
        # Meghívjuk a szülőosztály (GeneralPage) konstruktorát
        super().__init__(browser)

    def load(self):
        """Megnyitja a Vinted bejelentkezés/regisztráció oldalát a böngészőben."""
        self.open_webpage(self.URL)

    def login_button_click(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[@data-testid="auth-select-type--register-switch"]//span'))).click()

    def login_with_email_button_click(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//span[@data-testid="auth-select-type--login-email"]//span'))).click()

    def input_username_or_email(self, email):
        email_field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "username")))
        email_field.clear()
        email_field.send_keys(email)

    def input_password(self, password):
        password_field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)

    def button_submit_click(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']"))).click()
