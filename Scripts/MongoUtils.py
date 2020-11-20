import pymongo
# from pymongo import MongoClient
class MongoDB: # Classes generally are camel-case, starting with uppercase
    def __init__(self, dbname):
        # the __init__ method is the class constructor, where you define
        # instance members.  We'll make conn an instance member rather
        # than a class level member
        self._conn = pymongo.MongoClient("143.110.191.155", 37217)
        self._db   = self._conn[dbname]
    def createCollection(self, name=""):

        return self._db[name]

    def create(database, collection, add_user):

        my_col = collection
        my_col.insert_many(add_user)

    def drop(database, collection):
        my_col = collection
        my_col.drop()


    def search(database, collection, query):
        my_col = collection
        my_doc = my_col.find(query)
        print("The value searched for:")
        for x in my_doc:
            print(x)


    def update(database, collection, query, newvalues):
        my_col = collection
        my_col.update(query, newvalues)
        print("Updated values")
        for x in my_col.find():
            print(x)


    def delete(database,collection,query):
        my_col = collection
        my_col.delete_one(query)
        print("Document Deleted!")

    def one_update(database,collection,query,newvalue):
        collection.update_one(query,newvalue)
    # def my_search(database,collection,query):
    #     collection.find(query)


