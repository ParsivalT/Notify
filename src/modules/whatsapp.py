import requests
from .config import LOG

# This class is responsible for managing the sending of WhatsApp messages.
class WhatsappSendNotify:
    def __init__(self, api_key, phone_number):
        """
        Initializes the WhatsappSendNotify class with the API key and phone number.

        Args:
            api_key (str): The API key for authentication with the WhatsApp API.
            phone_number (str): The phone number to which messages will be sent.
        """
        self.base_url = f"https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={{}}&apikey={api_key}"
        LOG.info("WhatsappSendNotify initialized with phone number: {}".format(phone_number))

    def send_message(self, message: str) -> bool:
        """
        Sends a WhatsApp message to the specified phone number.

        Args:
            message (str): The message to be sent.
                Example: 'hello'

        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        if not message:
            LOG.warning("Attempted to send an empty message.")
            return False
            
        url = self.base_url.format(message)
        
        try: 
            response = requests.post(url)
            if response.status_code == 200:
                return True
            else:
                LOG.error("Failed to send message. Status code: {}, Response: {}".format(response.status_code, response.text))
                raise ConnectionError("There was a problem with the request.")

        except Exception as err:
            LOG.error(f"Error sending message: {err}")
            return False
