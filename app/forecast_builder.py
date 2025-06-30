"""
A series of functions to build each component of the forecast using the user
provided data.
"""
###############################################################################
# IMPORTS
###############################################################################
# Datetime combines date and time info. Imported as 'dt' for readability.
from datetime import datetime as dt

# Functions to call the APIs are imported from their relevant file
from apis.sun_api import sun_api_call
from apis.visualcrossing_api import lunar_api_call, cloud_api_call
from apis.auroraslive_api import aurora_api_call

# Utils are imported for datetime formatting and data transformation
from utils.datetime_utils import convert_to_24hr, reformat_iso8601
from utils.data_utils import find_how_cloudy, find_moon_phase

# Logging modules
from logger import logging_setup


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)


###############################################################################
# FORECAST BUILD FUNCTIONS
###############################################################################
def sun_forecast_build(dates: list, user_lat: float, user_lng: float) -> dict:
    """
    Builds a dictionary of the sun rise/set and twilight times for the given
    dates and location.

    For each date, it:
    - Calls the sun_api_call function to get sunrise/sunset/twilight times.
    - Formats the date as a string.
    - Removes unwanted keys like 'day_length' and 'solar_noon'.
    - Converts times to 24-hour format.

    Parameters:
        dates (list): List of datetime.date objects.
        user_lat (float): Latitude of the user.
        user_lng (float): Longitude of the user.

    Returns:
        dict: A nested dictionary keyed by date with sun event times.
    """
    logger.info('Running sun_forecast_build.')

    sun_forecast = {}
    for day in dates:
        # Running sun_api_call function to get sun and twilight times
        sun_api_response = sun_api_call(lat=user_lat, lng=user_lng, day=day)
        # Formatting the date into the specified string format
        day_str = dt.strftime(day, '%Y-%m-%d')
        # Using the day string to populate the sun_forecast dictionary with the
        # results section of the API response
        sun_forecast[day_str] = sun_api_response['results']
        # Removing unwanted data points from sun_forecast
        sun_forecast[day_str].pop('day_length', None)
        sun_forecast[day_str].pop('solar_noon', None)
    # For loop that loops through the top level of sun_forecast
    for _, forecast_times in sun_forecast.items():
        # Each day has a dictionary of times. This for loop loops through the
        # dictionary of times.
        for key, time in forecast_times.items():
            # Convert times to 24-hour clock using convert_to_24hr function
            forecast_times[key] = convert_to_24hr(time)
    logger.debug(f'sun_forecast is {sun_forecast}')
    return sun_forecast


def vc_forecast_build(vc_api_key: str,
                      dates: list,
                      user_lat: float,
                      user_lng: float
                      ) -> list | None:
    """
    Builds a list of two dictionaries when a user API key is provided. One
    dictionary is for the lunar forecast and one is or the cloud forecast.

    If an Visual Crossing API key is provided, for each date it:
    - Calls the lunar_api_call function to get moon rise and set times and the
        moon phase.
    - Extracts the moon rise and set times from the response.
    - Extracts the moon phase value and calls find_moon_phase function to
    convert this to a descriptive name.
    - Calls the cloud_api_call function to get the level of cloud cover.
    - Extracts the level of cloud cover from the API response.
    - Uses the find_how_cloudy function to add a descriptive forecast.

    Parameters:
        vc_api_key (str): user's API key for Visual Crossing.
        dates (list): List of datetime.date objects.
        user_lat (float): Latitude of the user.
        user_lng (float): Longitude of the user.

    Returns:
        List: a list with two nested dictionaries. The first dictionary is the
        lunar forecast keyed by date with moon rise/set times and phase. The
        second dictionary is the cloud cover forecast keyed by date.
        None: in the case a user API key is not given, None is returned.
    """
    logger.info('Running vc_forecast_build.')

    lunar_forecast = {}
    cloud_forecast = {}
    if vc_api_key != 'xxx':
        # Running the lunar_api_call function.
        lunar_api_response = lunar_api_call(lat=user_lat,
                                            lng=user_lng,
                                            start_date=dates[0],
                                            end_date=dates[-1],
                                            api_key=vc_api_key)
        # API call returns None for invalid API key. This if statement checks
        # None has not been returned
        if lunar_api_response is not None:
            # Using a for loop to format the API response and populate the
            # lunar_forecast dictionary
            for day in lunar_api_response['days']:
                day_str = day['datetime']
                day.pop('datetime', None)
                # Adding each day's lunar information to the lunar_forecast
                # dictionary with the date at the key.
                lunar_forecast[day_str] = day
                # Converting the moon phase percentage into a descriptive name
                # using the find_moon_phase function.
                lunar_forecast[day_str]['moonphase'] = find_moon_phase(
                    lunar_forecast[day_str]['moonphase'])

            logger.debug(f'lunar_forecast is: {lunar_forecast}')
            # Cloud and lunar have the same API key so cloud can remain in the
            # if statement
            # Running the cloud function with the user's location and for the
            # full three days.
            cloud_api_response = cloud_api_call(lat=user_lat,
                                                lng=user_lng,
                                                start_date=dates[0],
                                                end_date=dates[-1],
                                                api_key=vc_api_key)
            # Using a for loop to format the API response and populate the
            # cloud_forecast dictionary.
            for day in cloud_api_response['days']:
                day_str = day['datetime']
                day.pop('datetime', None)
                # Adding an entry with a descriptive forecast of the cloud
                # cover using the find_how_cloudy function.
                day['cloudforecast'] = find_how_cloudy(day['cloudcover'])
                # Adding cloud cover information to the cloud_forecast
                # dictionary with the date at the key.
                cloud_forecast[day_str] = day
            logger.debug(f'cloud_forecast is: {cloud_forecast}')
            return [lunar_forecast, cloud_forecast]
    return None


def aurora_forecast_build(dates: list,
                          user_lat: float,
                          user_lng: float) -> list:
    """
    Builds a list of two dictionaries containing the probability of seeing an
    aurora on the first night and a longer three day forecast.

    It:
    - Calls the aurora_api_call function for probability of auroras at the
      user's location.
    - Extracts the probability from the API response and stores it in a dict.
    - Calls the aurora_api_call function for the three day aurora forecast.
    - Extracts the three-day forecast from from the API response
    - Reformats the times within the forecast from ISO 8601 to a more readable
      form.

    Parameters:
        dates (list): List of datetime.date objects.
        user_lat (float): Latitude of the user.
        user_lng (float): Longitude of the user.

    Returns:
        List: a list of two nested dictionaries. The first dictionary contains
        the likelihood of seeing the aurora that evening, while the second
        gives a three-day probability forecast.
    """
    logger.info('Running aurora_forecast_build.')

    aurora_prob = {}
    aurora_3day = {}
    # Running the aurora_api_call function to call the API and receive the
    # probability data
    aurora_prob_api_response = aurora_api_call(
        lat=user_lat, lng=user_lng, data='probability')
    # Populating the aurora_prob dictionary with information from the full API
    # response
    aurora_prob['Probability'] = aurora_prob_api_response['value']
    aurora_prob['Colour'] = aurora_prob_api_response['colour']

    logger.debug(f'aurora_prob is: {aurora_prob}')
    # Running the aurora_api_call function to call the API and receive the
    # three-day forecast data.
    aurora_3day_api_response = aurora_api_call(
        lat=user_lat, lng=user_lng, data='threeday')
    # aurora_3day_api_response['values'] is a list with three lists of
    # dictionaries. The following zips this list to the dates list, creating a
    # dictionary with an item for each day.
    aurora_3day_zip = dict(zip(dates, aurora_3day_api_response['values']))
    # Simplifying aurora_3day_zip for readability using dictionary
    # comprehensions to iterate through aurora_3day_zip and the list of each
    # time period's forecast.
    aurora_3day = {
        date: [
            {
                # Using the reformat_iso8601 to format the start and end time
                # of each period more clearly
                'Start Time': reformat_iso8601(period['start']),
                'End Time': reformat_iso8601(period['end']),
                'Colour Status': period['colour'],
                'Kp Value': period['value']
            }
            # Dictionary comprehension for individual time periods in the list
            for period in periods
        ]
        # Dictionary comprehension for each day in aurora_3day_zip
        for date, periods in aurora_3day_zip.items()
    }
    logger.debug(f'aurora_3day is: {aurora_3day}')
    return [aurora_prob, aurora_3day]
