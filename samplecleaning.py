import pymongo
import sys
import pandas as pd
import numpy as np
from pymongo import MongoClient

#connect to Database
connection = MongoClient('localhost', 27017)
db = connection.newsdata

#handle newsdatac collection
data = db.samplecleaning
newsDataList = pd.DataFrame(list(data.find()))
#newsDataList = newsDataList[['_id', 'publication','date','title','author','content']]
print(newsDataList)
