"""
This file contains functions to collect user inputs.
"""
###############################################################################
# IMPORTS
###############################################################################
# Function that prints a how to message
from utils.message_utils import api_key_how_to

# Logging modules
from logger import logging_setup


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)

###############################################################################
# COLLECTING USER INPUT
###############################################################################
def collect_length() -> int:
    """
    Uses a while loop with try and except to collect the user's desired
    forecast length.
    """
    forecast_length = None
    while True:
        try:
            forecast_length = int(
                input('Would you like a 1, 2, or 3 day forecast? [1][2][3] '))
        except ValueError:
            logger.warning('User input invalid forecast length')
            print('Please enter 1, 2, or 3 aas numerals.')
            continue
        if 1 <= forecast_length <= 3:
            break
        logger.warning('User input invalid forecast length')
        print('Please enter a number between 1 and 3')
        continue
    logger.debug(f'Collected forecast length: {forecast_length}')
    return forecast_length


def collect_lat() -> float:
    """
    Uses a while loop with try and except to collect the user's latitude.
    """
    user_lat = None
    while True:
        try:
            user_lat = float(
                input('Please enter your latitude [-90 to 90]: ').strip())
        except ValueError:
            logger.warning('User input invalid latitude')
            print('Please enter your latitude as a decimal number.')
            continue
        if -90.0 <= user_lat <= 90.0:
            break
        logger.warning('User input invalid latitude')
        print('Your latitude should be between -90 and 90.')
        continue
    logger.debug(f'Collected user latitude: {user_lat}')
    return user_lat


def collect_lng() -> float:
    """
    Uses a while loop with try and except to collect the user's longitude.
    """
    user_lng = None
    while True:
        try:
            user_lng = float(
                input('Please enter your longitude [-180 to 180]: ').strip())
        except ValueError:
            logger.warning('User input invalid longitude')
            print('Please enter your longitude as a decimal number.')
            continue
        if -180.0 <= user_lng <= 180.0:
            break
        logger.warning('User input invalid longitude')
        print('Your longitude should be between -180 and 180.')
        continue
    logger.debug(f'Collected user longitude: {user_lng}')
    return user_lng


def api_key_instructions():
    """
    Uses a while loop with try and except to ask the user if they would like
    instructions on how to set up a Visual Crossing API key.
    """
    while True:
        visual_crossing_info = input(
            'Would you like to know how to get an API key for Visual '
            'Crossing? [YES][NO] ').strip()
        if visual_crossing_info.lower() == 'yes':
            api_key_how_to()
            break
        elif visual_crossing_info.lower() == 'no':
            break
        else:
            print('Please input yes or no.')
            continue


def collect_api_key():
    """
    Uses a while loop to collect the user's Visual Crossing API key.
    """
    API_key = None
    while True:
        API_key = input('Please enter your API key for visualcrossing.com\n'
                        'Enter "xxx" for no key but skip getting a lunar or '
                        'cloud forecast: ').strip()
        if API_key == 'xxx':
            break
        elif len(API_key) == 25:
            break
        else:
            print('Please enter your API key or "xxx".')
            continue
    logger.debug(f'Collected user API key: {API_key}')
    return API_key
