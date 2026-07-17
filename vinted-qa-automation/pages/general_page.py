import time

class GeneralPage:
    def __init__(self, browser):
        self.browser = browser  # Csak a böngészőt mentjük el

    def open_webpage(self, url):  # Az URL-t inkább itt kérjük el, ha meg kell nyitni valamit
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()

    def get_current_url(self):
        return self.browser.current_url

    def get_title(self):
        return self.browser.title

    def save_screenshot(self, filename: str):
        full_filename = f"{filename}_{int(time.time())}.png"
        self.browser.save_screenshot(full_filename)