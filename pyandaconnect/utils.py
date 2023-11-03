import requests


def response_decorator(response_function):
    """
    Decorator used to check the response of a GET request
    :param response_function: requests.get()
    :return: json object
    """

    def inner_response_wrapper(self, *args, **kwargs):

        # Attempts request
        try:
            res = response_function(self, *args, **kwargs)
            res.raise_for_status()
            return res.json()

        # Error handling
        except requests.exceptions.HTTPError as err_h:
            print("Http Error:", err_h)

        except requests.exceptions.ConnectionError as err_c:
            print("Error Connecting:", err_c)

        except requests.exceptions.Timeout as err_t:
            print("Timeout Error:", err_t)

        except requests.exceptions.RequestException as err:
            print("Error:", err)

    return inner_response_wrapper
