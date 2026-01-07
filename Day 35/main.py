import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

#example= https://api.openweathermap.org/data/2.5/weather?lat=40.7441172&lon=10.99&appid=85c353c698b935f4a943a1638de7a388
OWMendpoint= "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_api_key")
weather_params = {
    "lat" :"40.7441172",
    "lon" :"-73.9026698",
    "appid": api_key,
    "exclude":"current, minutely, daily"
}

Twillio_account_sid =os.environ.get("Twillio_account_sid")
Twillio_auth_token = os.environ.get("Twillio_auth_token")

response = requests.get(OWMendpoint,params=weather_params)
response.raise_for_status()
weather_data =response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    client = Client(Twillio_account_sid, Twillio_auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella☔",
        from_="+18776110160",
        to="+19147279719",
    )
    print(message.status)
else:
    from twilio.rest import Client

    client = Client(Twillio_account_sid, Twillio_auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It won't be rainy today",
        to='whatsapp:+19147279719'
    )

    print(message.sid)


# print(weather_data["hourly"][0]["weather"][0]["id"])