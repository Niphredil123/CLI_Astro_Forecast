"""
WELCOME TO STARGAZING FORECASTER!
This app is designed to receive a desired forecast length and location before
returning a forecast for stargazing conditions.
It will write a stargazing forecast to a text file listing:
- Sunrise and sunset times.
- The times of the different types of twilight.
- The rise and set times of the moon and its phase.
- The predicted cloud cover overnight.
- An aurora forecast.
"""
###############################################################################
# IMPORTS
###############################################################################
# Function to print welcome message
from utils.message_utils import welcome_message

# User input functions
from input_handler import api_key_instructions, collect_length
from input_handler import collect_api_key, collect_lat, collect_lng

# Functions to create a list of dates
from utils.datetime_utils import get_forecast_dates

# Functions to build each component of the forecast
from forecast_builder import sun_forecast_build, vc_forecast_build
from forecast_builder import aurora_forecast_build

# Function to output the forecast to a file
from output_writer import forecast_output


###############################################################################
# VARIABLES
###############################################################################
from config import FOLDER_NAME


###############################################################################
# SCRIPT
###############################################################################
# Introduction
welcome_message()

# Asking if the user wants to know how to create an API key for Visual Crossing.
api_key_instructions()

# Collecting user input
vc_api_key = collect_api_key()
forecast_length = collect_length()
user_lat = collect_lat()
user_lng = collect_lng()

# Producing date list based on forecast length
dates = get_forecast_dates(forecast_length)

# Build forecasts
sun_forecast = sun_forecast_build(dates, user_lat, user_lng)
vc_forecasts = vc_forecast_build(vc_api_key, dates, user_lat, user_lng)
aurora_forecast = aurora_forecast_build(dates, user_lat, user_lng)

# Write forecast file
output_success = forecast_output(dates,
                                 sun_forecast,
                                 vc_forecasts,
                                 aurora_forecast)

if output_success == 0:
    print(
        f'[SUCCESS!] file "Stargazing_Forecast.txt" has been saved '
        f'to the folder "{FOLDER_NAME}".')
