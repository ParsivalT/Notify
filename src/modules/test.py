from config import USER_AGENT, PROXIES
import random
import requests


user_agent = {
    'User-Agent' : random.choice(USER_AGENT) 
}
print(type(user_agent))

response = requests.get('https://wtfismyip.com/json', proxies=PROXIES, headers=user_agent)
print(response.text)
