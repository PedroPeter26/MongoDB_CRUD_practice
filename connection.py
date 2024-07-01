import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv('MONGODB_URI'))

db = client['iotDB']
db.create_collection('UberDB')
# accounts_collection = db['accounts']
for db_name in client.list_database_names():
    print(db_name)
