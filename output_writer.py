"""
This file contains the function to write the final forecast to a file.
"""
###############################################################################
# IMPORTS
###############################################################################
# Importing from datetime
from datetime import datetime as dt
from datetime import date

# Logging modules
from logger import logging_setup


###############################################################################
# VARIABLES
###############################################################################
# Define today
today = date.today()


###############################################################################
# SETUP LOGGING
###############################################################################
logger = logging_setup(__name__)


###############################################################################
# FUNCTIONS
###############################################################################
def forecast_output(dates: list,
                    sun_forecast: dict,
                    vc_forecasts: list | None,
                    aurora_forecast: list) -> int:
    """
    Function to write the forecasts to a file, 'Stargazing_Forecast.txt'.

    Parameters:
        dates (list): List of the dates for the forecast.
        sun_forecast (dict): Dictionary of the solar and twilight times.
        vc_forecasts (list): List of two dictionaries. One for the moon
            forecast and one for the cloud forecast. Is None if no API key is
            given.
        aurora_forecast (list): List of two dictionaries. One with tonight's
            aurora probability and one with a three-day forecast.

    """
    logger.info('Running forecast_output.')
    if vc_forecasts is not None:
        lunar_forecast = vc_forecasts[0]
        cloud_forecast = vc_forecasts[1]

    aurora_prob = aurora_forecast[0]
    aurora_3day = aurora_forecast[1]
    with open('Stargazing_Forecast.txt', 'w') as textfile:
        # Loop through each day in dates.
        for days in dates:
            # Formatting the day as a string, to be used as a dict key
            day_str = dt.strftime(days, '%Y-%m-%d')
            textfile.write('FORECAST FOR ' + day_str + '\n\n')
            textfile.write('SUN AND TWILIGHT\n')
            for key, value in sun_forecast[day_str].items():
                textfile.write('%s: %s\n' % (key, value))
            # Check if and API key was given and write to file if it was
            if vc_forecasts is not None:
                textfile.write('\n\nLUNAR\n')
                for key, value in lunar_forecast[day_str].items():
                    textfile.write('%s: %s\n' % (key, value))
                textfile.write('\n\nCLOUDS\n')
                # Selecting the cloud_forecast entries needed
                textfile.write(cloud_forecast[day_str]['cloudforecast'] + '\n')
                textfile.writelines(
                    str(cloud_forecast[day_str]['hours']) + '\n')
            else:
                textfile.write(
                    '\n\nNo API key provided for lunar and cloud cover '
                    'forecasts\n')
            textfile.write('\n\nAURORA\n')
            # If the current day in the for loop is today, give the aurora
            # probability forecast, else give the three-day.
            if days == today:
                textfile.write('The probability of seeing the aurora is ' +
                               str(aurora_prob['Probability']) +
                               '.\nThe colour status is ' +
                               str(aurora_prob['Colour']) + '.\n')
            else:
                # Writing only the last two entries of the current day's
                # aurora forecast to limit it to nighttime.
                for key, value in aurora_3day[days][-2].items():
                    textfile.write('%s: %s\n' % (key, value))
                for key, value in aurora_3day[days][-1].items():
                    textfile.write('%s: %s\n' % (key, value))
            textfile.write(
                '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                '~~~~~~~~~~~~~~~~\n\n')
    return 0
