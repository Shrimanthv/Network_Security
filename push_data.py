import os
import sys
import json


from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL= os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from Networksecurity.logging.logger import logging
from Networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def cv_to_json_convertor(self,filepath):
        try:
            data= pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.records=records
            self.database= database
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)

            self.database= self.mongo_client[self.database]
            self.collection=self.database[self.collection]

            self.collection.insert_many(self.records)

            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        


if __name__=="__main__":
    FILE_PATH="Network_data\phisingData.csv"
    DATABASE="data"
    Collection="networkdata"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(filepath=FILE_PATH)
    print(records)
    no_of_records= networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        