from flask import Flask
from pymongo import MongoClient

from lib.config_service import ConfigService

app = Flask(__name__)


@app.before_request
def init_mongo():
    g.mongo = MongoClient(ConfigService.get_mongo_host(), 27017).food_recipes


if __name__ == '__main__':
    app.run(debug=True, port=5001)
