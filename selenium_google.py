class SeleniumGoogle:
    def __init__(self, credentials, chrome_driver):
        self.credentials = credentials
        self.driver = chrome_driver
        self.tab_id = None

    def login(self):
        url = 'https://myaccount.google.com/'
        self.driver.get(url)
        self.tab_id = self.driver.current_window_handle
