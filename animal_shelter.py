
from pymongo import MongoClient
from bson.objectid import ObjectId

from bson.json_util import dumps
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:41564/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert(data)  # data should be dictionary
            # Check insertSuccess for operation
            if insertSuccess is not None:
                status = False
            # default return
            else:
                status = True
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            animalsCollection = self.database.animals.find(data, {"_id": False})
            #return a cursor object
            return animalsCollection
        else:
            raise Exception("No search criteria provided!")
            
# Creating method to implement the U in CRUD.
    def update(self, data, update_data):
        #check that search criteria was sufficiently provided, else raise exception
        if data is not None:
            #Results of the query to be stored as variable
            updateCollection = self.database.animals.update_many(data, update_data)

            #save results as variable
            result = "Documents updated: " + json.dumps(updateCollection.modified_count)
            #return new result
            return result
        else:
            raise Exception("Invalid Input Entered")

# Creating a method to implement D in CRUD.
    def delete(self, data):
        #check that search criteria was sufficiently provided, else raise exception
        if data is not None:
            #results of the query to be stored as variable
            deleteCollection = self.database.animals.delete_many(data)
            #save results of delete as variable
            result = "Documents Deleted: " + json.dumps(deleteCollection.deleted_count)
            #return result
            return result
        else:
            raise Exception("Invalid Input Entered")
