import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]

# mycol = mydb["customers"]

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")