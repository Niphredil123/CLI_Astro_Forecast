"""
Functions relating to the http://auroraslive.io API.
"""
###############################################################################
# IMPORTS
###############################################################################
# Importing requests to handle calling API urls.
# It may be necessary to pip install requests
import requests

# Logging modules
import logging
from logger import logging_setup

###############################################################################
# VARIABLES
###############################################################################
from config import AURORA_API_URL


###############################################################################
# SETUP LOGGING
###############################################################################
logging_setup()


###############################################################################
# FUNCTIONS
###############################################################################
def aurora_api_call(lat: float, lng: float, data: str) -> dict | None:
    """
    Calls http://auroraslive.io/#/api/v1 API (no key needed) to request an
    aurora forecast.

    It takes in user latitude and longitude, and a specification of
    data type to return data, converting to API  parameters before calling the
    API.

    Function parameters:
        lat (float): Latitude of the user.
        lng (float): Longitude of the user.
        data (str): What element of data to request from the API

    API parameters:
        type: which module of the API is to be called.
        tz: adjust for the timezone. At present, it is manually adjusted to
        British Summer Time.
        data: which data from the ace module should be returned 'threeday'
        and 'probability' will be used in this app.
    """
    logging.info('Running aurora_api_call.')

    params = {
        'type': 'ace',
        'lat': lat,
        'long': lng,
        'tz': -60,
        'data': data
    }
    response = requests.get(AURORA_API_URL, params=params, timeout=10)
    # Checking request was successful by looking for status code 200 and
    # returning the API response in a JSON format
    if response.status_code == 200:
        return response.json()
    # If the status code is not 200, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call auroraslive.io')
    return None
