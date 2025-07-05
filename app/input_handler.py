"""
This file contains functions to collect user inputs.
"""
###############################################################################
# IMPORTS
###############################################################################
# Function that prints a how to message
from utils.message_utils import api_key_how_to
from utils.validation_utils import validate_length, validate_lat, validate_lng, validate_yes_no, validate_key

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
        user_input = input(
            'Would you like a 1, 2, or 3 day forecast? [1][2][3] ')
        try:
            forecast_length = validate_length(user_input)
            break
        except ValueError as e:
            if str(e) == "Not Int":
                print("Please enter 1, 2, or 3 as numerals.")
            else:
                print("Please enter a number between 1 and 3")
            continue
    logger.debug('Collected forecast length: %s', forecast_length)
    return forecast_length


def collect_lat() -> float:
    """
    Uses a while loop with try and except to collect the user's latitude.
    """
    user_lat = None
    while True:
        user_input = input('Please enter your latitude [-90 to 90]: ')
        try:
            user_lat = validate_lat(user_input)
            break
        except ValueError as e:
            if str(e) == 'Not float':
                print('Please enter your latitude as a decimal number.')
            else:
                print('Your latitude should be between -90 and 90.')
            continue
    logger.debug('Collected user latitude: %s', user_lat)
    return user_lat


def collect_lng() -> float:
    """
    Uses a while loop with try and except to collect the user's longitude.
    """
    user_lng = None
    while True:
        user_input = input('Please enter your longitude [-180 to 180]: ')
        try:
            user_lng = validate_lng(user_input)
            break
        except ValueError as e:
            if str(e) == 'Not float':
                print('Please enter your longitude as a decimal number.')
            else:
                print('Your longitude should be between -180 and 180.')
            continue
    logger.debug('Collected user latitude: %s', user_lng)
    return user_lng


def api_key_instructions() -> None:
    """
    Uses a while loop with try and except to ask the user if they would like
    instructions on how to set up a Visual Crossing API key.
    """
    while True:
        user_input = input(
            'Would you like to know how to get an API key for Visual '
            'Crossing? [YES][NO] ')
        try:
            visual_crossing_info = validate_yes_no(user_input)
            if visual_crossing_info:
                api_key_how_to()
                break
            if not visual_crossing_info:
                break
        except ValueError:
            print('Please input yes or no.')
            continue


def collect_api_key():
    """
    Uses a while loop to collect the user's Visual Crossing API key.
    """
    api_key = None
    while True:
        user_input = input('Please enter your API key for visualcrossing.com\n'
                        'Enter "xxx" for no key but skip getting a lunar or '
                        'cloud forecast: ')
        try:
            api_key = validate_key(user_input)
            logger.debug('Collected user API key: %s', api_key)
            return api_key
        except ValueError:
            print('Please enter your API key or "xxx".')
            continue
