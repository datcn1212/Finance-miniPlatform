import redis

"""
Redis Event for get event data
db: 0
key for get data: 'event'
key for error data: 'err_event'
format: Redis list
"""
class Redis:

    def __init__(self, logger, host, port, db, event_key, error_event_key):
        self.logger = logger
        self.event_key = event_key
        self.error_event_key = error_event_key
        self.redis_event = redis.StrictRedis(host, port, db, charset="utf-8", decode_responses=True)
        self.logger.info("Connected to Redis Event at index %s", db)   

    def get_event_data(self, start, end):
        res = self.redis_event.lrange(self.event_key, start, end)
        return res
               
    def trim_event_data(self, start, end = -1):
        """
        trim event data [0,-1] to  [start, end]
        example:  {'key': 'event', value: [0,1,2,3]} -> ltrim(event, 1, -2): value:[1,2]
        """ 
        self.redis_event.ltrim(self.event_key, start, end)
        self.logger.info('Deleted got data from Redis: %d event', start)

        
    def count_event_len(self):
        res = self.redis_event.llen(self.event_key)
        self.logger.info('Length of key %s: %d', self.event_key, res)
        return res
    
    def insert_error_event(self, error_data):
        for data in error_data:
            self.redis_event.rpush(self.error_event_key, data)
        self.logger.info('Inserted to Redis %d error events', len(error_data))
        
        

