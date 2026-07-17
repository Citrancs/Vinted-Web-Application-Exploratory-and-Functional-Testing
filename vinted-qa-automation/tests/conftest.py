import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--guest')
    options.add_argument('--lang=hu')
    # options.add_argument('--headless') # Ha háttérben futtatnád

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # Itt fut le maga a teszt

    driver.quit()  # A teszt végén bezárja a böngészőt