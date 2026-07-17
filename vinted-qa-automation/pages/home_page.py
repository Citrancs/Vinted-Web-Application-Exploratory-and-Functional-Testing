from pages.general_page import GeneralPage

class HomePage(GeneralPage):
    URL = "https://www.vinted.hu"

    def __init__(self, browser):
        # Meghívjuk a szülőosztály (GeneralPage) konstruktorát
        super().__init__(browser)

    def load(self):
        """Megnyitja a Vinted főoldalát a böngészőben."""
        self.open_webpage(self.URL)