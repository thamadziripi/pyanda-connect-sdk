import unittest
from pyandaconnect.account import Account


class TestAccountInfo(unittest.TestCase):
    def test_account_id(self):
        account_id = "123456"
        api = Account()
        api.set_account_id(account_id)
        self.assertEqual(api._account_id, account_id)

    def test_account_id_arg(self):
        account_id = "123456"
        api = Account(account_id=account_id)
        self.assertEqual(api._account_id, account_id)

    def test_get_account_list(self):
        account_api = Account()
        res = account_api.get_account_summary()
        self.assertEqual(type(res), str)


if __name__ == '__main__':
    unittest.main()
