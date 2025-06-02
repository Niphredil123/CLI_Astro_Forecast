"""
Functions relating to the https://www.visualcrossing.com API.
"""
###############################################################################
# IMPORTS
###############################################################################
# Date class represents a calendar date.
from datetime import date

# Importing requests to handle calling API urls.
# It may be necessary to pip install requests
import requests

# Logging modules
from logger import logging_setup


###############################################################################
# VARIABLES
###############################################################################
from config import VC_API_URL


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)


###############################################################################
# FUNCTIONS
###############################################################################
def lunar_api_call(lat: float,
                   lng: float,
                   start_date: date,
                   end_date: date,
                   api_key: str) -> dict | None:
    """
    Call API at https://www.visualcrossing.com to receive moon rise and set
    times and moon phase.
    Take in user latitude and longitude, and the start and end date of the
    forecast.

    API parameters:
        unitGroup: specifies that the results should be in metric units.
        key: the user API key.
        include: specifies that the information should be given per day.
        elements: lists the desired lunar facts.
    """
    logger.info('Running lunar_api_call.')

    location_date = str(lat) + ',' + str(lng) + '/' + str(start_date) + '/' \
        + str(end_date)
    params = {
        'unitGroup': 'metric',
        'key': api_key,
        'include': 'days',
        'elements': 'datetime,moonphase,moonrise,moonset'
    }

    try:
        # Try to call Visual Crossing with the params and location/dat string
        response = requests.get(VC_API_URL + location_date,
                                params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        # Raise and log an exception if the connection times out.
        logger.exception(f'{VC_API_URL} timed out')
    except requests.exceptions.ConnectionError:
        # Raise and log an exception for a connection error.
        logger.exception(f'Failed to connect to {VC_API_URL}')
    except requests.exceptions.HTTPError:
        # Raise and log an exception if the status code is for 4xx or 5xx errors
        logger.exception(f'{VC_API_URL} gave an unsuccessful status code')
        # 401 is unauthorised request
        if response.status_code == 401:
            print('Your API key is invalid. You will not get a lunar or cloud'
                  'forecast.')
    except requests.exceptions.RequestException:
        # Raise and log all other request exceptions.
        logger.exception(f'An error occurred calling {VC_API_URL}')
    else:
        logger.debug(f'Lunar API response is: {response}')
        # Checking request was successful by looking for status code 200 and
        # returning the API response in a JSON format
        if response.status_code == 200:
            return response.json()
    # If an error occurred, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call https://weather.visualcrossing.com '
          'for lunar info')
    return None


def cloud_api_call(lat: float,
                   lng: float,
                   start_date: date,
                   end_date: date,
                   api_key: str) -> dict | None:
    """
    Call API at https://www.visualcrossing.com to receive daily and hourly
    cloud cover information.
    Take in user latitude and longitude, and the start and end date of the
    forecast.

    API Parameters:
        unitGroup: specifies that the results should be in metric units.
        key: the user API key.
        include: specifies that the cloud information should be given per hour.
        elements: requests cloud cover predictions and datetime of cloud cover
        predictions.
    """
    logger.info('Running cloud_api_call.')

    location_date = str(lat) + ',' + str(lng) + '/' + str(start_date) + '/' + \
        str(end_date)
    params = {
        'unitGroup': 'metric',
        'key': api_key,
        'include': 'hours',
        'elements': 'datetime,cloudcover'
    }

    try:
        # Try to call Visual Crossing with the params and location/dat string
        response = requests.get(VC_API_URL + location_date, params=params,
                                timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        # Raise and log an exception if the connection times out.
        logger.exception(f'{VC_API_URL} timed out')
    except requests.exceptions.ConnectionError:
        # Raise and log an exception for a connection error.
        logger.exception(f'Failed to connect to {VC_API_URL}')
    except requests.exceptions.HTTPError:
        # Raise and log an exception if the status code is for 4xx or 5xx errors
        logger.exception(f'{VC_API_URL} gave an unsuccessful status code')
        # 401 is unauthorised request
        if response.status_code == 401:
            print('Your API key is invalid. You will not get a lunar or cloud'
                  'forecast.')
    except requests.exceptions.RequestException:
        # Raise and log all other request exceptions.
        logger.exception(f'An error occurred calling {VC_API_URL}')
    else:
        logger.debug(f'Cloud API response is: {response}')
        # Checking request was successful by looking for status code 200 and
        # returning the API response in a JSON format
        if response.status_code == 200:
            return response.json()
    # If an error occurred, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call https://weather.visualcrossing.com '
          'for cloud info')
    return None
