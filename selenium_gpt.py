import util


class SeleniumGPT:
    def __init__(self, credentials, chrome_driver):
        self.credentials = credentials
        self.driver = chrome_driver
        self.tab_id = None

    def login(self):
        url = 'https://chat.openai.com/'
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)
        self.tab_id = self.driver.current_window_handle