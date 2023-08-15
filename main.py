import pymongo
import pandas as pd

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://sakethchoudary227:Skqgi9782@cluster0.v079hz2.mongodb.net/?retryWrites=true&w=majority")

# Database Name
dataBase = client["store_sales"]

# Collection  Name
collection = dataBase['train']

# Lets Verify all the record at once present in the record with all the fields
data = pd.DataFrame(list(i for i in collection.find()))
data.drop('_id',axis=1,inplace=True)
data.to_csv("base data.csv")


