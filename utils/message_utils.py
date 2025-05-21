"""
Simple print functions with larger messages for the user.
"""
###############################################################################
# IMPORTS
###############################################################################
# Logging modules
import logging
from logger import logging_setup


###############################################################################
# SETUP LOGGING
###############################################################################
logging_setup()


###############################################################################
# FUNCTIONS
###############################################################################
def welcome_message():
    print(
        '''
        ================================================================================
        WELCOME TO STARGAZING FORECASTER!
        This app takes your location and desired forecast length and writes a stargazing
        forecast to a text file listing:
        - Sunrise and sunset times.
        - The times of the different types of twilight.
        - The rise and set times of the moon and its phase.
        - The predicted cloud cover overnight.
        - An aurora forecast.
        It uses three APIs: https://sunrise-sunset.org, https://www.visualcrossing.com,
        and http://auroraslive.io.
        Only Visual Crossing requires an API key. The app will ask you to input your
        API key for Visual Crossing. You can skip entering an API key; however, if you
        do this, you will not receive a lunar or cloud forecast.
        ================================================================================
        '''
    )


def api_key_how_to():
    print(
        '''
        To register for an API Key with Visual Crossing:
        - Go to [this link](https://www.visualcrossing.com/weather-data-editions) and
          choose the free plan.
        - Enter your email and the validation code sent to that email.
        - Choose a password and agree to the Ts&Cs.
        - Enter a description of why you are using the API. A suggested answer is:
            'Creating a program for personal use that will give conditions for
            stargazing'
        - Click create account.
        - Sign in to your new account.
        - Click on 'Account' in the top right hand corner of the window to find you
          API key under your details.
        '''
    )
