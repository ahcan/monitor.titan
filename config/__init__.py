from setting import titan_ip, account
from os import path, remove
import logging
import logging.config
import logging.handlers
import json

with open("config/logging_configuration.json", 'r') as configuration_file:
    config_dict = json.load(configuration_file)
logging.config.dictConfig(config_dict)
# Create the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
