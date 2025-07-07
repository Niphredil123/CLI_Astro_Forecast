"""
This file contains the util functions used to validate user inputs.
"""
###############################################################################
# IMPORTS
###############################################################################
# Regex
import re

# Logging modules
from logger import logging_setup


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)


###############################################################################
# FUNCTIONS
###############################################################################
def validate_length(value: str) -> int:
    """
    Validates user input is an integer between 1 and 3 for the forecast length.
    """
    try:
        forecast_length = int(value.strip())
    except ValueError as e:
        logger.warning('User input invalid forecast length: not int')
        raise ValueError('Not Int') from e
    if 1 <= forecast_length <= 3:
        return forecast_length
    logger.warning('User input invalid forecast length: out of range')
    raise ValueError('Out of forecast range')


def validate_lat(value: str) -> float:
    """ Validates user input is a float between -90 and 90 for latitude"""
    try:
        user_lat = float(value.strip())
    except ValueError as e:
        logger.warning('User input invalid latitude: not float')
        raise ValueError('Not float') from e
    if -90.0 <= user_lat <= 90.0:
        return user_lat
    logger.warning('User input invalid latitude: out of range')
    raise ValueError('Invalid latitude')


def validate_lng(value: str) -> float:
    """ Validates user input is a float between -180 and 180 for longitude"""
    try:
        user_lng = float(value.strip())
    except ValueError as e:
        logger.warning('User input invalid longitude: not float')
        raise ValueError('Not float') from e
    if -180.0 <= user_lng <= 180.0:
        return user_lng
    logger.warning('User input invalid longitude: out of range')
    raise ValueError('Invalid longitude')


def validate_yes_no(value: str) -> bool:
    """Check if user input is yes or no."""
    yes_no = value.strip().lower()
    if yes_no in ('yes', 'y'):
        return True
    if yes_no in ('no', 'n'):
        return False
    raise ValueError('Invalid input')


def validate_key(value: str) -> str:
    """
    Checks user api key is a valid api key or 'xxx' for no key.
    No specific format for the API key could be found, but the length 
    seems to be 25 characters.
    """
    api_key = value.strip()
    if re.match(r'^[xX]{3}$', api_key):
        return api_key.lower()
    if len(api_key) == 25:
        return api_key
    raise ValueError('Invalid input')
