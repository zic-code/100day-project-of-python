import requests
#
# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
#
# data = res.json()
#
# longitude =data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude,longitude)
#
# print(iss_position)

parameters = {
    "lat":40.743770,
    "lng":-73.902638,
    "tzid": "EST",
    "formatted":0
}


response = requests.get(url="https://api.sunrise-sunset.org/json",params= parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
