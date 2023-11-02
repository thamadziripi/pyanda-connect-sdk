from pyandaconnect.account import Account
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    # Env variables
    env_cars = load_dotenv()
    token = os.environ.get("AUTH_TOKEN")
    account = os.environ.get("ACCOUNT_ID")

    # Account api
    account_api = Account(account_id=account)
    account_api.set_access_token(token)

    # Get account details
    print(account_api.get_account_summary())
