from elasticsearch import Elasticsearch
import json
fp = open('/Users/admin/Downloads/Hamshahri-Query_Judgement/final4.txt', encoding='utf8').readlines()

es = Elasticsearch()
for x in fp:
    load = json.loads(x,strict=False)
    print (x)
    es.index(index='hamshahri-final', doc_type='articles',id=load['DID'],  body=load)
    # print(load['DID'])
