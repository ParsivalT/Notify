import schedule
from time import sleep
from functools import partial
import sys
from modules import config, whatsapp, crypto_hub
from modules.messagens import MessageTemplates

# Check for essential configurations
if not config.API_KEY or not config.PHONE_NUMBER:
    config.LOG.error("API_KEY and PHONE_NUMBER must be set in the environment variables.")
    sys.exit("Error: API_KEY and PHONE_NUMBER are required. Exiting the program.")

coins_list = config.COINS

# Responsible for controlling notifications.
notification_status = {coin["name"]: {"sent_max": False, "sent_min": False} for coin in coins_list}

whats = whatsapp.WhatsappSendNotify(config.API_KEY, config.PHONE_NUMBER)
COIN = crypto_hub.HubCrypto()

def check_price(coins: list):
    for coin in coins:
        current_p = COIN.price_consult(coin["name"], coin["country_coin"])
        config.LOG.info(f"Current price for {coin['name']}: {current_p}")

        if current_p >= coin["value_max"] and not notification_status[coin["name"]]["sent_max"]:
            if not config.DEVELOPMENT:  # Correção aqui
                whats.send_message(MessageTemplates.value_above.format(coin["name"], coin["ticket"], current_p))

            notification_status[coin["name"]]["sent_max"] = True
            config.LOG.info(f"Notification sent: {coin['name']} exceeded max value.")
            continue

        if current_p <= coin["value_min"]:
            if not config.DEVELOPMENT:
                whats.send_message(MessageTemplates.value_below.format(coin["name"], coin["ticket"], current_p))
                
            notification_status[coin["name"]]["sent_min"] = True
            config.LOG.info(f"Notification sent: {coin['name']} fell below min value.")
            continue

        config.LOG.info(f"No action needed for {coin['name']}.")

        # Wait 5 seconds 
        sleep(5)

def send_current_price(coins: list):
    for coin in coins:
        current_p = COIN.price_consult(coin["name"], coin["country_coin"])
        if not config.DEVELOPMENT:
            whats.send_message(MessageTemplates.reminder.format(coin["name"].title(), coin["ticket"].upper(), current_p))
        config.LOG.info(f"Sent current price for {coin['name']}: {current_p}")
        sleep(5)

def reset_notification_status(coins: list):
    config.LOG.info("Resetting notification statuses.")
    for coin in coins:
        current_p = COIN.price_consult(coin["name"], coin["country_coin"])

        if coin["value_max"] > current_p:
            notification_status[coin["name"]]["sent_max"] = False

        if coin["value_min"] < current_p:
            notification_status[coin["name"]]["sent_min"] = False

# Scheduling tasks
schedule.every(10).minutes.do(partial(check_price, coins_list))
schedule.every(1).hour.do(partial(send_current_price, coins_list))
schedule.every(1).hour.do(partial(reset_notification_status, coins_list))

def main():
    send_current_price(coins_list)
    
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    main()
