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
from logger import logging_setup


###############################################################################
# VARIABLES
###############################################################################
from config import SUN_API_URL


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)


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
    logger.info('Running sun_api_call.')

    params = {
        'lat': lat,
        'lng': lng,
        'date': day,
        'tzid': 'Europe/London'
    }
    try:
        # Trying to call the Sun API using the params
        response = requests.get(SUN_API_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        # Raise and log an exception if the connection times out.
        logger.exception(f'{SUN_API_URL} timed out')
    except requests.exceptions.ConnectionError:
        # Raise and log an exception for a connection error.
        logger.exception(f'Failed to connect to {SUN_API_URL}')
    except requests.exceptions.HTTPError:
        # Raise and log an exception if the status code is for 4xx or 5xx errors
        logger.exception(f'{SUN_API_URL} gave an unsuccessful status code')
    except requests.exceptions.RequestException:
        # Raise and log all other request exceptions.
        logger.exception(f'An error occurred calling {SUN_API_URL}')
    else:
        logger.debug(f'Sun API response is: {response}')
        # Checking request was successful by looking for status code 200 and
        # returning the API response in a JSON format
        if response.status_code == 200:
            return response.json()
    # If an error occurred, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call https://sunrise-sunset.org/')
    return None
