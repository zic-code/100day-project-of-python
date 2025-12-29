import requests
from datetime import datetime
import time
import smtplib

MY_LAT = -23.746109 # Your latitude
MY_LONG = -38.90195 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "EST"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True

def send_email():
    my_email = "jisoostest@gmail.com"
    app_password = "pgtg ghbd hity mkpp"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="leejisoo910413@gmail.com",
                            msg=f"Subject: iss is upside \n\n The iss is above you in the sky.")

while True:
    time.sleep(60)
    if is_iss_overhead():
        if is_night():
            send_email()
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



