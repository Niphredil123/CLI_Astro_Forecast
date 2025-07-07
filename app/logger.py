"""
File to set up logging.
"""
###############################################################################
# IMPORTS
###############################################################################
import configparser
import logging
import os

from logging.handlers import RotatingFileHandler


###############################################################################
# VARIABLES
###############################################################################
# Load config file and log details
config = configparser.ConfigParser()
config.read('config.ini')

# Load config info from config.ini
MAX_SIZE = int(config.get('logging', 'log_max_size', fallback='30000'))
BACKUP_COUNT = int(config.get('logging', 'log_backup_count', fallback='3'))
log_folder = config.get('logging', 'log_folder', fallback='logs')
log_file = config.get('logging', 'log_file', fallback='.log')
log_level = config.get('logging', 'log_level'.upper(), fallback='DEBUG')
log_format = config.get('logging', 'log_format', fallback='%%(asctime)s - %%(name)s')

# Check logging folder exists
log_path = os.path.join(log_folder, log_file)
os.makedirs(os.path.dirname(log_path), exist_ok=True)


###############################################################################
# LOGGING SET UP
###############################################################################
def logging_setup(name: str):
    """
    Function to setup logging.
    Returns a configured logger with rotating file handling.
    """
    # Create logger
    logger = logging.getLogger(name)

    # If loop to prevent adding multiple handlers
    if not logger.handlers:
        logger.setLevel(getattr(logging, log_level, logging.INFO))

        # Setting up file handler to rotate through logs
        file_handler =RotatingFileHandler(log_path, maxBytes=MAX_SIZE,
                                        backupCount=BACKUP_COUNT)

        # Setting log format and applying to file handler
        file_handler.setFormatter(logging.Formatter(log_format))
        file_handler.setLevel(getattr(logging, log_level, logging.INFO))

        # add handler
        logger.addHandler(file_handler)

        # Prevent log messages being passed to root logger
        logger.propagate = False

    return logger
