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


###############################################################################
# VARIABLES
###############################################################################
from config import VC_API_URL


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
    location_date = str(lat) + ',' + str(lng) + '/' + \
        str(start_date) + '/' + str(end_date)
    params = {
        'unitGroup': 'metric',
        'key': api_key,
        'include': 'days',
        'elements': 'datetime,moonphase,moonrise,moonset'
    }
    response = requests.get(VC_API_URL + location_date,
                            params=params, timeout=10)
    # Checking request was successful by looking for status code 200 and
    # returning the API response in a JSON format
    if response.status_code == 200:
        return response.json()
    # 401 is unauthorised request
    elif response.status_code == 401:
        print('Your API key is invalid. You will not get a lunar or cloud'
              'forecast.')
        return None
    # If the status code is not 200, the app will print that the API call was
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
    location_date = str(lat) + ',' + str(lng) + '/' + \
        str(start_date) + '/' + str(end_date)
    params = {
        'unitGroup': 'metric',
        'key': api_key,
        'include': 'hours',
        'elements': 'datetime,cloudcover'
    }
    response = requests.get(VC_API_URL + location_date,
                            params=params, timeout=10)
    # Checking request was successful by looking for status code 200 and
    # returning the API response in a JSON format
    if response.status_code == 200:
        return response.json()
    # 401 is unauthorised request
    elif response.status_code == 401:
        print('Your API key is invalid. You will not get a moon or cloud '
              'forecast.')
        return None
    # If the status code is not 200, the app will print that the API call was
    # unsuccessful and return None
    print('An error occurred trying to call https://weather.visualcrossing.com '
          'for cloud info')
    return None
