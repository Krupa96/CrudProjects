from Scripts.MongoUtils import MongoDB
database = MongoDB("TestUtilDB")
collection = database.createCollection("Customers")


def create(add_user):
    MongoDB.create(database, collection, add_user)


def my_search(query):
    MongoDB.search(database, collection, query)


def update(query, new_value):
    MongoDB.update(database, collection, query, new_value)


def oupdate(query, new_value):
    MongoDB.one_update(database, collection, query, new_value)


def delete(query):
    MongoDB.delete(database, collection, query)


def drop():
    MongoDB.drop(database, collection)








