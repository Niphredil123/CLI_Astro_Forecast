###############################################################################
# IMPORTS
###############################################################################
import os

###############################################################################
# GLOBAL VARIABLES
###############################################################################
# Folder name
FOLDER_NAME = os.getcwd().split('\\')[-1]

# API urls
SUN_API_URL = 'https://api.sunrise-sunset.org/json'
VC_API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
AURORA_API_URL = 'http://api.auroras.live/v1/'
