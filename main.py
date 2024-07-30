import os

import util
from browser import BrowserSessionManager
from selenium_auth import SeleniumZerodha
from selenium_google import SeleniumGoogle
from selenium_gpt import SeleniumGPT
from zerodha import ZerodhaClient

# load credentials
yaml_file_path = os.path.expanduser('~/.zerodha/credentials.yaml')
credentials = util.load_credentials(yaml_file_path)

# create global browser instance
browser = BrowserSessionManager(credentials).get_browser()

# login into google
selenium_google_client = SeleniumGoogle(credentials, browser).login()

# login into Zerodha
selenium_zerodha_client = SeleniumZerodha(credentials, browser)
request_token = selenium_zerodha_client.get_request_token()

# login into chatgpt
selenium_gpt_client = SeleniumGPT(credentials, browser).login()

# get portfolio from zerodha
zerodha_client = ZerodhaClient(credentials)
zerodha_client.login(request_token)
zerodha_client.get_holdings()
input('waiting for input')
