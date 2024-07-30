from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BrowserSessionManager:
    def __init__(self, credentials):
        self.browser = None
        self.credentials = credentials
        self.profile_path = self.credentials['profile_path']

    def start_browser(self):
        service = Service(r'/usr/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f"--user-data-dir={self.profile_path}")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-infobars")
        self.browser = webdriver.Chrome(service=service, options=options)

    def get_browser(self):
        if self.browser is None:
            self.start_browser()
        return self.browser

    def close_browser(self):
        if self.browser:
            self.browser.quit()
            self.browser = None
