###############################################################################
# IMPORTS
###############################################################################
import configparser
import logging
import os


###############################################################################
# LOGGING SET UP
###############################################################################
# Load config and set lof file and level
config = configparser.ConfigParser()
config.read('config.ini')

log_file = config['logging']['log_file']
log_level = config['logging']['log_level'].upper()

# Check logging folder exists
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Set logging configuration
logging.basicConfig(
    filename=log_file,
    level=getattr(logging, log_level),
    format='%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(funcName)s'
)
