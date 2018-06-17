import pymongo
import sys
import pandas as pd
import numpy as np
from pymongo import MongoClient

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#---------connect to Database----------

connection = MongoClient('localhost', 27017)
db = connection.newsdata

#----------handle newsdatac collection----------

data = db.samplecleaning
newsDataList = pd.DataFrame(list(data.find()))
newsDataList = newsDataList[['_id', 'publication','title','content','author','date','cleaned']]


#---------start cleaning---------

#set _id as unique identifier to refer each tuple
newsDataList['_id'].is_unique
newsDataList.set_index('_id', inplace=True)
newsDataList.head()

print(newsDataList)
