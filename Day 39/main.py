#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
from dotenv import load_dotenv
import requests

load_dotenv()
#env setting
sheety_authorization = os.environ.get("sheety_authorization")

Object_id=""
#GET & POST
sheety_endpoint ="https://api.sheety.co/59fe5b883f7384758981549d46fd6bd4/flightDeals/prices"
#put
sheety_put_endpoint = f"{sheety_endpoint}/{Object_id}"
#headers
headers= {
    "Authorization" : sheety_authorization
}
response = requests.get(url=sheety_endpoint, headers = headers)
pprint(response)