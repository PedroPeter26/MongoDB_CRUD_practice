import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError

class MongoHandler:
    def __init__(self):
        pass

    def mongoConnect(self, database):
        load_dotenv()
        try:
            client = MongoClient(os.getenv('MONGODB_URI'),
                                 connectTimeoutMS=7000,
                                 socketTimeoutMS=7000,
                                 serverSelectionTimeoutMS=7000
            )
            client.server_info()
            print("Connected to MongoDB successfully")
            db = client[database]
            return db
        except (ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError) as e:
            print(f"Connection failed: {e}")
            return False

    def mongoInsertOne(self, database, collection, data):
        db = self.mongoConnect(database)
        if db is None:
                return False
        collection = db[collection]
        try:
            result = collection.insert_one(data)
            document_id = result.inserted_id
            print(f"_id of inserted document: {document_id}")
            return True
        except Exception as e:
            print(f"Error al insertar el documento: {e}")
            return False
        finally:
            if db is not None:
                db.client.close()

    def mongoInsertMany(self, database, collection, data):
        db = self.mongoConnect(database)
        if db:
            collection = db[collection]
            result = collection.insert_many(data)
            document_ids = result.inserted_ids
            print(f"_id of inserted documents: {document_ids}\n")
            print("# of documents inserted: " + str(len(document_ids)))
            return True
        else:
            return False

    def mongoShowDocs(self, database, collection):
        db = self.mongoConnect(database)
        if db:
            collection = db[collection]
            result = collection.find()
            print(list(result))
            return True
        else:
            return False

    def mongoUpdateOne(self, database, collection, _id, data):
        db = self.mongoConnect(database)
        if db:
            collection = db[collection]
            result = collection.update_one({'_id': _id}, {'$replaceWith': data})
            print(result)
            return True
        else:
            return False

    def mongoDeleteOne(self, database, collection, _id):
        db = self.mongoConnect(database)
        if db:
            collection = db[collection]
            result = collection.delete_one({'_id': _id})
            print(result)
            return True
        else:
            return False
