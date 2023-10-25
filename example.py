from pyandaconnect.authentication import Authenticate

if __name__ == '__main__':
    api = Authenticate(silent=False)
    api.set_api_key("222sy")
    api.authenticate_api()