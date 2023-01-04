#-------------------------MAIN PROGRAM------------------------------------
import logging.config
import configparser

from vnstock import * 
import pandas

#-------------------Set logging config------------------------------------
logging.basicConfig(level = logging.DEBUG, filename="./logs/log.txt", format='---%(asctime)s: %(message)s', filemode='a')
logger = logging.getLogger()

#-------------------Read config file--------------------------------------
config = configparser.ConfigParser()
config.read('./src/config/config.ini')


#-------------------Get data from API-------------------------------------

listing_companies()

ticker_overview('TCB')

df =  stock_historical_data(symbol='GMD', start_date="2021-01-01", end_date='2022-09-22')

price_board('TCB,SSI,VND') # so sanh cac ticker

stock_intraday_data(symbol='GMD', page_num=0, page_size=5000) # giao dich trong ngay

#------------------Push got data to Redis---------------------------------- 


#------------------Get data from Redis and insert to Spark/Hadoop----------


#------------------Insert to Elasticsearch---------------------------------


#------------------Apache Airflow------------------------------------------


