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

#Load variable from
log_folder = config['logging']['log_folder']
log_file = config['logging']['log_file']
log_level = config['logging']['log_level'].upper()
max_size = int(config['logging']['log_max_size'])
backup_count = int(config['logging']['log_backup_count'])
log_format = config['logging']['log_format']

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
        file_handler =RotatingFileHandler(log_path, maxBytes=max_size,
                                        backupCount=backup_count)

        # Setting log format and applying to file handler
        file_handler.setFormatter(logging.Formatter(log_format))
        file_handler.setLevel(getattr(logging, log_level, logging.INFO))

        # add handler
        logger.addHandler(file_handler)

        # Prevent log messages being passed to root logger
        logger.propagate = False

    return logger
