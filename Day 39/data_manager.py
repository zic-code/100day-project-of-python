import os
from pprint import pprint
from dotenv import load_dotenv
import requests

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/59fe5b883f7384758981549d46fd6bd4/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._auth = os.environ["sheety_authorization"]
        self.destination_data = {}
    def get_destination_data(self):
        headers = {
            "Authorization" : self._auth
        }
        response = requests.get(url= SHEETY_PRICES_ENDPOINT, headers =headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
