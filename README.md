# STARGAZING FORECASTER

This CLI app is designed to receive a desired forecast length (up to three
days) and location (lat and long) before returning a forecast for stargazing
conditions.

It will write a stargazing forecast to a text file listing:
- Sunrise and sunset times.
- The times of the different types of twilight.
- The rise and set times of the moon and its phase.
- The predicted cloud cover overnight.
- An aurora forecast.

## Installation
1. Clone the repo.
2. Create and activate a virtual environment (optional, but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

## Usage
### To run the app you will need:
- Python 3.10+
- An internet connection
- Your longitude and latitude
- A Visual Crossing API key (optional)

### To run the app:
1. Navigate to the project folder in the terminal
2. Enter:
```bash
python3 main.py
```
3. You will be prompted to enter your:
    - Visual Crossing API key (optional)
    - Desired forecast length (1-3 days)
    - Latitude and Longitude
4. The app will call the web APIs and write a file `Stargazing_Forecast.txt` to the folder.

## Project Folder Structure
```
stargazer/
├── main.py                 # Orchestrates input, API calls, and output
├── config.py               # Constants and default settings
├── messages.py             # Print functions for large messages
├── input_handler.py        # User input collection and validation
├── forecast_builder.py     # Forecast logic (combines API responses)
├── output_writer.py        # Writes the forecast to file
├── apis/
│   ├── auroraslive_api.py          # Aurora API call
|   ├── sun_api.py                  # Solar API call
│   └── visualcrossing_api.py       # Moon and cloud API call
├── utils/
│   ├── data_utils.py               # Data transform utils
│   └── datetime_utils.py           # Datetime utils
```

## APIs
The app relies on three APIs:
- [Sunrise Sunset](https://sunrise-sunset.org) collects:
    - Sunrise time
    - Sunset time
    - Twilight times
- [Visual Crossing](https://www.visualcrossing.com) collects:
    - Moon rise time
    - Moon set time
    - Moon phase
    - Cloud cover
- [Auroras Live](http://auroraslive.io) collects:
    - Aurora probability

Of these, only Visual Crossing requires the user to register for an API key,
the other two are open APIs. The app will ask you to input your API key for
Visual Crossing. There is an option to skip entering an API key by entering
`xxx`; however, if you do this, you will not receive a moon or cloud forecast.

### Getting a Visual Crossing API Key
This information is also provided when running the app from the console, but to
register for an API Key with Visual Crossing:
1. Go to [this link](https://www.visualcrossing.com/weather-data-editions) and
choose the free plan.
2. Enter your email and the validation code sent to that email.
3. Choose a password and agree to the Ts&Cs.
4. You will have to enter a description of why you are using the API. A
suggested answer is:
    > 'Creating a program for personal use that will give conditions for
    stargazing'
5. Click create account.
6. Sign in to your new account.
7. Click on 'Account' in the top right hand corner of the window to find you
API key under your details.

## Example Output
```
FORECAST FOR 2025-05-18

SUN AND TWILIGHT
sunrise: 04:58
sunset: 21:02
civil_twilight_begin: 04:15
civil_twilight_end: 21:45
nautical_twilight_begin: 03:11
nautical_twilight_end: 22:49
astronomical_twilight_begin: 01:00
astronomical_twilight_end: 01:00


LUNAR
moonphase: Waning gibbous
moonrise: 01:55:16
moonset: 09:13:18


CLOUDS
It is too cloudy for good stargazing.
[{'datetime': '00:00:00', 'cloudcover': 85.0}, {'datetime': '01:00:00', 'cloudcover': 90.2}, {'datetime': '02:00:00', 'cloudcover': 83.5}, {'datetime': '03:00:00', 'cloudcover': 74.3}, {'datetime': '04:00:00', 'cloudcover': 75.4}, {'datetime': '05:00:00', 'cloudcover': 96.1}, {'datetime': '06:00:00', 'cloudcover': 94.5}, {'datetime': '07:00:00', 'cloudcover': 95.0}, {'datetime': '08:00:00', 'cloudcover': 95.0}, {'datetime': '09:00:00', 'cloudcover': 95.0}, {'datetime': '10:00:00', 'cloudcover': 94.5}, {'datetime': '11:00:00', 'cloudcover': 94.5}, {'datetime': '12:00:00', 'cloudcover': 94.5}, {'datetime': '13:00:00', 'cloudcover': 61.9}, {'datetime': '14:00:00', 'cloudcover': 70.4}, {'datetime': '15:00:00', 'cloudcover': 84.8}, {'datetime': '16:00:00', 'cloudcover': 95.9}, {'datetime': '17:00:00', 'cloudcover': 100.0}, {'datetime': '18:00:00', 'cloudcover': 100.0}, {'datetime': '19:00:00', 'cloudcover': 100.0}, {'datetime': '20:00:00', 'cloudcover': 100.0}, {'datetime': '21:00:00', 'cloudcover': 69.6}, {'datetime': '22:00:00', 'cloudcover': 74.3}, {'datetime': '23:00:00', 'cloudcover': 35.1}]


AURORA
The probability of seeing the aurora is 0.
The colour status is green.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```


## Acknowledgements
[Sunrise Sunset](https://sunrise-sunset.org)  
[Visual Crossing](https://www.visualcrossing.com)  
[Auroras Live](http://auroraslive.io)  