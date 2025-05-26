"""
Functions relating to transforming datetime information.
"""
###############################################################################
# IMPORTS
###############################################################################
# Importing classes from datetime to handle all the times and dates in the app.
from datetime import date
from datetime import datetime as dt
from datetime import timedelta


###############################################################################
# DEFINING FUNCTIONS
###############################################################################
def get_forecast_dates(length):
    """ Returns a list of dates based on the requested forecast length. """
    today = date.today()
    return [today + timedelta(days=i) for i in range(length)]


def convert_to_24hr(timestr: str) -> str:
    """
    Converts the 12-hour clock to the 24-hour clock in hours and minutes.
    """
    time_obj = dt.strptime(timestr, '%I:%M:%S %p')
    return time_obj.strftime('%H:%M')


def reformat_iso8601(dt_str: str) -> str:
    """
    Uses string slicing to convert an ISO 8601 datetime string to a readable
    format.
    """
    return dt_str[:10] + ' - ' + dt_str[11:16]
