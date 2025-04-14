import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
user_email = os.getenv("USER_EMAIL")

MY_LAT = -15 # Your latitude
MY_LONG = -33 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_nighttime():
    if sunset < time_now.hour:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=user_email,
                msg="Subject: Look up!\n\nHello Wesley!\n\nLook up! The ISS is overhead.\n\nKind Regards,\n\nDahlia."
            )
        print("Hello Wesley!\n\nLook up! The ISS is overhead.\n\nKind Regards,\n\nDahlia.")
    elif time_now.hour < sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=user_email,
                msg="Subject: Look up!\n\nHello Wesley!\n\nLook up! The ISS is overhead.\n\nKind Regards,\n\nDahlia."
            )
        print("Subject: Look up!\n\nHello Wesley\n\nLook up! The ISS is overhead.\n\nKind Regards,\n\nDahlia.")
    else:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=user_email,
                msg="Subject: ISS OVERHEAD\n\nHello Wesley!\n\nThe ISS is overhead, but it's too bright to see."
                    "\n\nKind Regards,\n\nDahlia."
            )
        print("Subject: ISS OVERHEAD\n\nHello Wesley!\n\nThe ISS is overhead, but it's too bright to see."
              "\n\nKind Regards,\n\nDahlia.")


def is_iss_overhead():
    if (MY_LAT - 5) < iss_latitude < (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
        is_nighttime()
    else:
        print(f"The ISS is not overhead.\nYour coordinates are: {MY_LAT, MY_LONG}\nISS coordinates are:"
              f"{iss_latitude, iss_longitude}.")


is_iss_overhead()
