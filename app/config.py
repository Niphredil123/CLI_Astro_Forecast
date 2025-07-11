"""
This module contains key configuration variables, parsing some from the
config.ini file.
"""
###############################################################################
# IMPORTS
###############################################################################
import configparser
import os


###############################################################################
# CONFIGURE VARIABLES
###############################################################################
# Reading Config info from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Folder name
FOLDER_NAME = os.getcwd().split('\\')[-1]

# API urls
SUN_API_URL = config['API']['SUN_API_URL']
VC_API_URL = config['API']['VC_API_URL']
AURORA_API_URL = config['API']['AURORA_API_URL']
