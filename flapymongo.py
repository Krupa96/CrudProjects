from flask import Flask
from Scripts.MongoHandlers  import my_search

app = Flask(__name__)


@app.route('/')
def hello_world():
    return my_search()
    return 'CRUD Operations on Mongo!'



if __name__ == '__main__':
    app.run()
