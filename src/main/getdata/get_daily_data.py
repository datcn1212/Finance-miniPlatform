from vnstock import * 
import pandas

class DailyData:

    def __init__(self, logger):
        self.logger = logger 

    def get_daily_data(self):

        listing_companies()

        ticker_overview('TCB')

        df =  stock_historical_data(symbol='GMD', start_date="2021-01-01", end_date='2022-09-22')

        price_board('TCB,SSI,VND') # so sanh cac ticker

        stock_intraday_data(symbol='GMD', page_num=0, page_size=5000) # giao dich trong ngay