import csv
import pickle

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    dic = {}
    for row in reader:
       k, v = row
       dic[k] = v
       output = open('data.pkl', 'wb')
       pickle.dump(dic, output)
       output.close()       



from elasticsearch import Elasticsearch
es = Elasticsearch()

es.index("ggw","artice", "gg",)