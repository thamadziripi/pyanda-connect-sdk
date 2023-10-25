

class Authenticate:
    def __init__(self, api_key: str = None, oauth_token: str = None, silent: bool = True):
        """
        A class which can be used to authenticate a user's account
        :param api_key: User's OANDA API Key
        :param oauth_token: User's OANDA authentication token
        """
        self._api_key = api_key
        self._oauth_token = oauth_token
        self.silent = silent

    def set_api_key(self, api_key: str = None):
        """
        Sets the API key attribute

        :param api_key: User's OANDA API Key
        :return: None
        """
        self._api_key = api_key

    def set_oauth_token(self, oath_token: str = None):
        """
        Sets the Authentication token
        :param oath_token: User's OANDA authentication token
        :return: None
        """
        self._oauth_token = oath_token

    def authenticate_api(self):
        """
        Authenticates user using either an API Key or Authentication token
        :return:
        """
        if self._api_key is not None:
            print(f'Authenticated using API key: {self._api_key}') if not self.silent else None
        elif self._oauth_token is not None:
            print(f'Authenticated using Authentication token: {self._oauth_token}') if not self.silent else None
        else:
            raise ValueError('No authentication information specified. Please set an API key or OAuth token')

