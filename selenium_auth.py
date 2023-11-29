import time
from urllib.parse import urlparse, parse_qs

import pyotp
from kiteconnect import KiteConnect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumZerodha:
    def __init__(self, credentials, driver):
        self.credentials = credentials
        self.driver = driver
        self.tab_id = None

    def get_request_token(self):
        self._login_to_zerodha()
        final_url = self._wait_for_redirect()
        return self._extract_request_token(final_url)

    def _get_login_url(self):
        kite = KiteConnect(api_key=self.credentials.get('api_key'))
        return kite.login_url()

    def _login_to_zerodha(self):
        url = self._get_login_url()
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)
        self.tab_id = self.driver.current_window_handle
        wait = WebDriverWait(self.driver, 30)

        self._fill_credentials()
        self._submit_login_form()
        self._fill_otp(wait)

    def _fill_credentials(self):
        wait = WebDriverWait(self.driver, 10)
        # user_id_input = wait.until(EC.presence_of_element_located((By.ID, 'userid')))
        password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        checkbox = self.driver.find_element(By.ID, 'checkbox-23')

        # user_id_input.send_keys(self.credentials.get('user_id'))
        password_input.send_keys(self.credentials.get('user_password'))
        self.driver.execute_script("arguments[0].click();", checkbox)

    def _submit_login_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'button-orange')))
        submit_button.click()

    def _fill_otp(self, wait):
        time.sleep(2)
        otp_input = wait.until(EC.presence_of_element_located((By.ID, 'userid')))
        totp = pyotp.TOTP(self.credentials.get('totp_secret'))
        otp_input.send_keys(totp.now())

    def _wait_for_redirect(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.url_matches(".*request_token=.*"))
        return self.driver.current_url

    def _extract_request_token(self, final_url):
        parsed_url = urlparse(final_url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get('request_token')[0]
