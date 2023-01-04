from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def gen_data(index, data=[]):
    for doc in data:
        yield {
            "_index": index,
            "_source": doc
        }


class ElasticSearch(object):

    def __init__(self, hosts, logger):
        self.logger = logger
        self.es_client = Elasticsearch(hosts=hosts)
        self.logger.info('Connected to Elasticsearch {}'.format(hosts))

    def insert_to_es(self, index, data=[]):
        bulk(self.es_client, gen_data(index, data))

    def create_index(self, mapping, name):
        if not self.es_client.indices.exists(index=name):
            response = self.es_client.indices.create(
                index=name,
                body=mapping
            )
            if response['acknowledged']:
                self.logger.info("Create index %s success", name)
                return True
            else:
                self.logger.error("Create in1dex $s fail", name)
                return False
        else:
            self.logger.info("%s index exitst", name)
        return True




