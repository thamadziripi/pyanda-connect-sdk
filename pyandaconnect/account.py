import requests
from pyandaconnect.authentication import Authenticate
from pyandaconnect.utils import response_decorator


class Account(Authenticate):
    def __init__(self, account_id: str = None, live_environment: bool = False):
        """
        A class containing methods to make GET requests on various account endpoints
        :param account_id: User's account identification
        :param live_environment: When True, the API uses a live account. Otherwise, it defaults a practice account.
        """

        super().__init__()

        # Captures user's account id
        self._account_id = account_id

        # Base URL for accounts endpoints
        self._account_endpoint = 'v3/accounts'

        # Endpoint for account details
        self._account_details_endpoint = f'{self._account_endpoint}/{self._account_id}'

        # Endpoint for account summary
        self._account_summary_endpoint = f'{self._account_endpoint}/{self._account_id}/summary'

        # Endpoint to return a list of tradeable instruments
        self._account_instrument_endpoint = f'{self._account_endpoint}/{self._account_id}/instruments'

        # Allows user to specify whether they want to use practice or live environment
        self._environment = f'https://api-fx{"trade" if live_environment else "practice"}.oanda.com'

    def set_account_id(self, account_id: str = None):
        """
        Sets the account id
        :param account_id: User's account ID
        :return: None
        """
        self._account_id = account_id

    @response_decorator
    def get_account_list(self):
        """
        A method used to return a list of accounts authorized for the given token.
        :return: json object
        """
        return requests.get(f'{self._environment}/{self._account_id}', headers=self.headers)

    @response_decorator
    def get_account_details(self):
        """
        A method used to get the full details of a single account that a client has access to.
        :return: json object
        """
        return requests.get(f'{self._environment}/{self._account_details_endpoint}', headers=self.headers)

    @response_decorator
    def get_account_summary(self):
        """
        A method used to get a summary of a single account that a client has access to.
        :return: json object
        """
        return requests.get(f'{self._environment}/{self._account_summary_endpoint}', headers=self.headers)

    @response_decorator
    def get_instruments(self):
        """
        A method used to get a list of tradeable instruments that an account has access to.
        :return: json object
        """
        return requests.get(f'{self._environment}/{self._account_instrument_endpoint}', headers=self.headers)
