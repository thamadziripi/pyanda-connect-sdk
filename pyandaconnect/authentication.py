

class Authenticate:
    def __init__(self, access_token: str = None, silent: bool = True):
        """
        A class which can be used to authenticate a user's account
        :param api_key: User's OANDA API Key
        :param oauth_token: User's OANDA authentication token
        """
        self._access_token = access_token
        self.silent = silent

    def set_access_token(self, access_token: str = None):
        """
        Sets the Authentication token

        :param access_token: User's OANDA access token
        :return: None
        """
        self._access_token = access_token


    def authenticate_api(self):
        """
        Authenticates user using either an API Key or Authentication token
        :return:
        """
        if self._access_token is not None:
            print(f'Authenticated using Authentication token: {self._access_token}') if not self.silent else None
        else:
            raise ValueError('No authentication information specified. Please set an API key or OAuth token')

