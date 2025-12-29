import requests

#example= https://api.openweathermap.org/data/2.5/weather?lat=40.7441172&lon=10.99&appid=85c353c698b935f4a943a1638de7a388
OWMendpoint= "https://api.openweathermap.org/data/3.0/onecall"
api_key = "64085ba3d08d5ec52ec6159ea3a16afc"
weather_params = {
    "lat" :"40.7441172",
    "lon" :"-73.9026698",
    "appid": api_key,
    "exclude":"current, minutely, daily"
}




response = requests.get(OWMendpoint,params=weather_params)
response.raise_for_status()
weather_data =response.json()
weather_slice = weather_data["hourly"][:12]

# print(weather_data["hourly"][0]["weather"][0]["id"])