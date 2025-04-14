# ISS Tracker App

This Python script tracks the International Space Station (ISS) in real time and checks whether it’s currently passing over your location **at night**, making it potentially visible in the sky.

If the ISS is overhead and it's dark enough to see it, the app will send an email notification to a specified address.

---

# Features

- Tracks the ISS location using a public API
- Checks sunrise and sunset times for your location
- Detects if the ISS is overhead *and* if it's dark outside
- (Optional) Sends an email notification if visibility conditions are met

---

# Requirements

- Python 3.6+
- `requests`
- `python-dotenv`

Install dependencies with:

pip install -r requirements.txt

# Usage

1. Clone repositry
2. Create .env file

MY_EMAIL=youremail@gmail.com
MY_PASSWORD=yourpassword
USER_EMAIL=recipient@example.com
SEND_EMAIL=false

3. Set your coordinates in main.py for example
MY_LAT=51.5074
MY_LONG=-0.1278

4. Run the app

