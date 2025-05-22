###############################################################################
# IMPORTS
###############################################################################
import configparser

import os


###############################################################################
# CONFIGURE VARIABLES
###############################################################################
# Folder name
FOLDER_NAME = os.getcwd().split('\\')[-1]


config = configparser.ConfigParser()
config.read('config.ini')

# API urls
SUN_API_URL = config['API']['SUN_API_URL']
VC_API_URL = config['API']['VC_API_URL']
AURORA_API_URL = config['API']['AURORA_API_URL']
