import requests
from .config import *


class HubCrypto:
    """
    A class to interact with the CoinGecko API for cryptocurrency price data.

    Methods
    -------
    price_consult(coin_name: str, country_coin: str = 'BRL') -> float:
        Retrieves the current price of a specified cryptocurrency in the desired currency.
    """

    def __init__(self):
        """
        Initializes the HubCrypto class with the base URL for the CoinGecko API.
        """
        self.base_url = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}&include_last_updated_at=true'
        self.headers = get_random_headers()
        self.proxies = PROXIES 

    def price_consult(self, coin_name: str, country_coin: str = 'BRL') -> float:
        """
        Consults the current price of a specified cryptocurrency.

        Parameters
        ----------
        coin_name : str
            The name of the cryptocurrency (e.g., 'bitcoin', 'monero').
        country_coin : str, optional
            The currency in which the price should be fetched (default is 'BRL').

        Returns
        -------
        float
            The current price of the specified cryptocurrency in the desired currency.
            Returns None if the price data is not found or an error occurs.
        """
        url = self.base_url.format(coin_name, country_coin)

        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies)
            LOG.info(f'New consult for crypto coin: {coin_name}')
            
            if response.status_code != 200:
                LOG.error(f"Error fetching quote for {coin_name}: {response.text}")
                raise ConnectionError(f"There was a problem with querying: {response.text}")

            data = response.json().get(coin_name)
            price = data.get(country_coin.lower())

            if price is None:
                LOG.warning(f"Price data not found for {coin_name} in {country_coin}")
                return None

            LOG.info(f"Retrieved price for {coin_name}: {price}")
            return float(price)

        except Exception as err:
            LOG.warning(f"Exception occurred: {err}")
            return None  # Return None in case of error

if __name__ == '__main__':
    cri = HubCrypto()
    cri.price_consult('monero')
