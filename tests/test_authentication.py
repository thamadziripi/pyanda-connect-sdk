import unittest
from pyandaconnect.authentication import Authenticate


class TestAuthentication(unittest.TestCase):
    def test_access_token(self):
        """
        First test case when using the set_access_token method
        """
        api = Authenticate()
        api_key = "xxxx-yyyy"
        api.set_access_token(api_key)
        self.assertEqual(api._access_token, api_key)

    def test_api_key_arg(self):
        """
        Second test case when using the access_token argument
        """
        api_key = "xxxx-yyyy"
        api = Authenticate(access_token=api_key)
        self.assertEqual(api._access_token, api_key)


if __name__ == '__main__':
    unittest.main()
