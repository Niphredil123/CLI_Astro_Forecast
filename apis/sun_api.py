"""
Functions relating to the https://sunrise-sunset.org API.
"""
###############################################################################
# IMPORTS
###############################################################################
# Date class represents a calendar date.
from datetime import date

# Importing requests to handle calling API urls.
import requests

# Logging modules
import logging
from logger import logging_setup


###############################################################################
# VARIABLES
###############################################################################
from config import SUN_API_URL


###############################################################################
# SETUP LOGGING
###############################################################################
logging_setup()


###############################################################################
# FUNCTIONS
###############################################################################
def sun_api_call(lat: float, lng: float, day: date) -> dict | None:
    """
    Call https://sunrise-sunset.org/api API (no key needed) to receive the
    sunrise, sunset, and twilight times. The function takes in the user's
    latitude and longitude and the date to use as parameters in the URL
    request. The API defaults to UTC time. For the purposes of this exercise,
    the timezone is set to Europe/London.
    """
    params = {
        'lat': lat,
        'lng': lng,
        'date': day,
        'tzid': 'Europe/London'
    }
    response = requests.get(SUN_API_URL, params=params, timeout=10)
    # Checking request was successful by looking for status code 200 and
    # returning the API response in a JSON format
    if response.status_code == 200:
        return response.json()
    # If the status code is not 200, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call https://sunrise-sunset.org/')
    return None
