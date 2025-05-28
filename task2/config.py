from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebdriverConfig:
    def __init__(self):
        driver = webdriver.Chrome(
            service=Service(executable_path=ChromeDriverManager().install()),
            options=self._get_webdriver_options()
        )
        wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

    @staticmethod
    def _get_webdriver_options():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "eager"
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        return chrome_options
