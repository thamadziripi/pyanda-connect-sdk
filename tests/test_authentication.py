import unittest
from pyandaconnect.authentication import Authenticate


class TestAuthentication(unittest.TestCase):
    def test_api_key(self):
        """
        First test case when using the set_api_key method
        """
        api = Authenticate()
        api_key = "xxxx-yyyy"
        api.set_api_key(api_key)
        self.assertEqual(api._api_key, api_key)

    def test_oath_token(self):
        """
        Second test case when using the set_oauth_token method
        """
        api = Authenticate()
        token = "xxxx-yyyy"
        api.set_oauth_token(token)
        self.assertEqual(api._oauth_token, token)

    def test_api_key_arg(self):
        """
        Third test case when using the api_key argument
        """
        api_key = "xxxx-yyyy"
        api = Authenticate(api_key=api_key)
        self.assertEqual(api._api_key, api_key)

    def test_oauth_token_arg(self):
        """
        Fourth test case when using the oath_token argument
        """
        token = "xxxx-yyyy"
        api = Authenticate(oauth_token=token)
        self.assertEqual(api._oauth_token, token)


if __name__ == '__main__':
    unittest.main()
