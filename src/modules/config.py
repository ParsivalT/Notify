import os
import logging
import sys
from dotenv import load_dotenv
import random

def get_random_headers() -> dict:
    user_agent = {
       'User-Agent': random.choice(USER_AGENT)
   } 
    return user_agent

# Config of directory
ROOT_DIRECTORY = os.getcwd()
LOG_DIRECTORY = os.path.join(ROOT_DIRECTORY, "logs")
load_dotenv(os.path.join(ROOT_DIRECTORY, 'src', ".env"))

DEVELOPMENT = os.getenv("DEV", "false").lower() == "true"

# ---------------------------LOGS CONFIG----------------------------
if not os.path.exists(LOG_DIRECTORY):
    print("Creating Directory: logs")
    os.mkdir(LOG_DIRECTORY)

LOG_FORMAT = 'Date/Time: %(asctime)s | LEVEL:%(levelname)s | Message:%(message)s'
logging.basicConfig(filename=os.path.join(LOG_DIRECTORY, "data.log"), level=logging.INFO, format=LOG_FORMAT)

# Adding console logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.stream = open(sys.stdout.fileno(), 'w', encoding='utf-8', errors='replace')
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

LOG = logging.getLogger()
LOG.addHandler(console_handler)
# ------------------------------------------------------------------

# Load environment variables from .env file.
API_KEY = os.getenv("API_KEY")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

if API_KEY is None:
    LOG.error("API_KEY not found in environment variables.")
    sys.exit("Error: API_KEY is required. Exiting the program.")

if PHONE_NUMBER is None:
    LOG.error("PHONE_NUMBER not found in environment variables.")
    sys.exit("Error: PHONE_NUMBER is required. Exiting the program.")

# ---------------------------COIN CONFIG---------------------------
COINS = [{
    "name": "monero",
    "ticket": "xmr",
    "country_coin": "USD",
    "value_min": 120.00,
    "value_max": 181.00
}, {
    "name": "bitcoin", 
    "ticket": "btc",
    "country_coin": "USD",
    "value_min": 57_000.00,
    "value_max": 68_000.00 
}]
# ------------------------------------------------------------------

# User_agent configs
USER_AGENT = [
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko']

# Proxy config
PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'  
}
