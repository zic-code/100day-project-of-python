import os
from dotenv import load_dotenv
import requests
from datetime import datetime

from requests.auth import HTTPBasicAuth

##date setting
now = datetime.now()
today = now.strftime("%Y/%m/%d")
now_time = now.strftime("%H:%M:%S")


## env setting
load_dotenv()
api_key = os.environ.get("nutrition_api_key")
app_id = os.environ.get("nutrition_app_id")
sheety_auth = os.environ.get("sheety_authorization")
sheety_username = os.environ.get("sheety_username")
sheety_password = os.environ.get("password")


## endpoint setting
base_URL= "https://app.100daysofpython.dev"
url_post= f"{base_URL}/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/59fe5b883f7384758981549d46fd6bd4/copyOfMyWorkouts/workouts"


header= {
    "x-app-id": app_id,
    "x-app-key": api_key
}
exercise_text = input("Tell me which exercises you did:")
post_data = {
    "query": exercise_text,
    "weight_kg": 90,
    "height_cm": 174,
    "age": 34,
    "gender": "male"
}
result = requests.post(url = url_post,json=post_data,headers=header).json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": sheety_auth
    }
    sheet_response = requests.post(sheet_endpoint,json= sheet_inputs,headers=headers)
    print(sheet_response.text)