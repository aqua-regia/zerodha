from kiteconnect import KiteConnect


class ZerodhaClient:
    def __init__(self, credentials):
        self.kite = None
        self.credentials = credentials

    def login(self, request_token):
        self.kite = self._create_kite_instance(request_token)

    def _create_kite_instance(self, request_token):
        api_key = self.credentials.get('api_key')
        api_secret = self.credentials.get('api_secret')

        kite = KiteConnect(api_key=api_key)
        access_token = self._generate_access_token(kite, request_token, api_secret)
        kite.set_access_token(access_token)
        return kite

    def _generate_access_token(self, kite, request_token, api_secret):
        data = kite.generate_session(request_token, api_secret=api_secret)
        return data["access_token"]

    def get_holdings(self):
        if self.kite is None:
            raise ValueError("Kite instance not created. Please login first.")
        holdings = self.kite.holdings()
        print(holdings)
