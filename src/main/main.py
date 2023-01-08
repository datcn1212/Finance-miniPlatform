#-------------------------MAIN PROGRAM------------------------------------
import logging.config
import configparser

from vnstock import * 
import pandas

from getdata.get_daily_data import DailyData
from dao.redis.redis_dao import Redis
from dao.elasticsearch.elastic_dao import ElasticSearch

from utils.validate_redis_data import *


#-------------------Set logging config------------------------------------
logging.basicConfig(level = logging.DEBUG, filename="./logs/log.txt", format='---%(asctime)s: %(message)s', filemode='a')
logger = logging.getLogger()

#-------------------Read config file--------------------------------------
config = configparser.ConfigParser()
config.read('./src/config/config.ini')

REDIS_HOST = config.get("REDIS", "host")
REDIS_PORT = config.get("REDIS", "port")
REDIS_DB = config.get("REDIS", "db")
REDIS_EVENT_KEY = config.get("REDIS", "event_key")
REDIS_ERROR_EVENT_KEY = config.get("REDIS", "error_event_key")
PAGE_SIZE = config.get("REDIS", "page_size")

ELASTIC_HOST = config.get("ELASTICSEARCH", "hosts")
#-------------------Get data from API and insert to Redis-------------------------------------

daily_data = DailyData(logger)

#------------------Get data from Redis and insert to Spark/Hadoop----------

def process_data_redis():
    """
    process data: validate number of data fields,...
    """
    logger.info('Processing Redis data...!')

    redis_event = Redis(logger, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_EVENT_KEY, REDIS_ERROR_EVENT_KEY)

    try:

        count_event_data = redis_event.count_event_len()

        while count_event_data > 0:
            logger.info('Processing %d events ...', count_event_data)

            raw_data = redis_event.get_event_data(0, int(PAGE_SIZE) - 1)  # get event data (len = page size)
            redis_event.trim_event_data(int(PAGE_SIZE), -1)  # pop above got data

            processed_data = validate_redis_data(raw_data)
            validated_data = processed_data[0]
            error_data = processed_data[1]

            if len(validated_data) > 0:
                #insert to Spark/Hadoop
                pass
            else:
                logger.info('No data validated!')

            if len(error_data) > 0:
                redis_event.insert_error_event(error_data)  # insert error data to Redis
                # process later
            else:
                logger.info('No error data!')

            count_event_data -= 1

        logger.info('Job completed...!')

    except Exception:
        logger.error("Exception: ", exc_info=True)

#------------------Insert to Elasticsearch---------------------------------


#------------------Apache Airflow------------------------------------------


