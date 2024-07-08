import os
import json
from bson import ObjectId
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
                                 connectTimeoutMS=5000,
                                 socketTimeoutMS=5000,
                                 serverSelectionTimeoutMS=5000
            )
            client.server_info()
            print("Connected to MongoDB successfully")
            db = client[database]
            return db
        except (ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError) as e:
            print(f"Connection failed: {e}")
            return None

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
        if db is None:
            return False
        collection = db[collection]
        try:
            result = collection.insert_many(data)
            document_ids = result.inserted_ids
            print(f"_id of inserted documents: {document_ids}\n")
            print("# of documents inserted: " + str(len(document_ids)))
            return True
        except Exception as e:
            print(f"Error al insertar los documentos: {e}")
            return False
        finally:
            if db is not None:
                db.client.close()

    def mongoShowDocs(self, database, collection):
        db = self.mongoConnect(database)
        if db is None:
            return False
        try:
            collection = db[collection]
            result = collection.find()
            for doc in result:
                print(json.dumps(doc, indent=4, default=str))
            return True
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return False
        finally:
            if db is not None:
                db.client.close()

    def mongoUpdateOne(self, database, collection, _id, data):
        db = self.mongoConnect(database)
        if db is None:
            return False
        try:
            collection = db[collection]
            result = collection.update_one({'_id': ObjectId(_id)}, {'$set': data})
            print(result)
            return True
        except Exception as e:
            print(f"Error al modificar el documento: {e}")
            return False
        finally:
            if db is not None:
                db.client.close()

    def mongoDeleteOne(self, database, collection, _id):
        db = self.mongoConnect(database)
        if db is None:
            return False
        try:
            collection = db[collection]
            result = collection.delete_one({'_id': ObjectId(_id)})
            print(result)
            return True
        except Exception as e:
            print(f"Error al eliminar el documento: {e}")
            return False
        finally:
            if db is not None:
                db.client.close()
                