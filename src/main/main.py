#-------------------------MAIN PROGRAM------------------------------------

import logging.config
import configparser

#-------------------Set logging config------------------------------------
logging.basicConfig(level = logging.DEBUG, filename="./logs/log.txt", format='---%(asctime)s: %(message)s', filemode='a')
logger = logging.getLogger()

#-------------------Read config file--------------------------------------
config = configparser.ConfigParser()
config.read('./src/config/config.ini')