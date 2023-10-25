import unittest
from pyandaconnect.account_info import AccountInfo


class TestAccountInfo(unittest.TestCase):
    def test_account_id(self):
        account_id = "123456"
        api = AccountInfo()
        api.set_account_id(account_id)
        self.assertEqual(api._account_id, account_id)

    def test_account_id_arg(self):
        account_id = "123456"
        api = AccountInfo(account_id=account_id)
        self.assertEqual(api._account_id, account_id)


if __name__ == '__main__':
    unittest.main()
