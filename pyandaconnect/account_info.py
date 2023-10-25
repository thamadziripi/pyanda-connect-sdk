import requests

class AccountInfo:
    def __init__(self, account_id: str = None, live_environment: bool = False):
        """
        A class which gets a user's account details
        :param account_id: User's account identification
        :param live_environment: When True, the API uses a live account. Otherwise, it defaults a practice account.
        """
        self._account_id = account_id

        if live_environment:
            self._environment = 'https://api-fxtrade.oanda.com'
        else:
            self._environment = 'https://api-fxpractice.oanda.com'

        # Instantiating different endpoints for account info
        self._account_endpoint = '/v3/accounts'
        self._account_details_endpoint = f'{self._account_endpoint}/{self._account_id}'
        self._account_summary_endpoint = f'{self._account_endpoint}/{self._account_id}/summary'
        self._account_instrument_endpoint = f'{self._account_endpoint}/{self._account_id}/instrument'
        self._account_changes_endpoint = f'{self._account_endpoint}/{self._account_id}/changes'

    def set_account_id(self, account_id: str = None):
        """
        Sets the account id
        :param account_id: User's account ID
        """
        self._account_id = account_id

    def get_account_list(self):
        """
        A method used to return a list of accounts authorized for the given token
        :return: json object
        """
        requests.get(f'{self._environment}/{self._account_id}')
