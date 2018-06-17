import pymongo
import sys
import pandas as pd
import numpy as np
from pymongo import MongoClient

#----------connect to Database-----------

connection = MongoClient('localhost', 27017)
db = connection.newsdata


#----------handle newsdatac collection----------

data = db.newsdatacoll
newsDataList = pd.DataFrame(list(data.find()))
newsDataList = newsDataList[['_id', 'publication','title','content','author','date','cleaned']]

pd.set_option('display.height', 1000)
pd.set_option('display.width', 1000)

#data1 = newsDataList[newsDataList.file == np.random.choice(data['publication': 'New York Times'].unique())].reset_index(drop=True)
#s= newsDataList.sample(n=100)
print(newsDataList)


#df = pd.read_csv('articles1.csv')
#df.head()
#print(df)
#sys.getsizeof(newsDataList)






