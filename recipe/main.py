from flask import Flask, g, request
from flask.json import jsonify
from pymongo import MongoClient

from lib import *

app = Flask(__name__)


def required_param(key):
    if not g.json_body:
        raise Exception("Missing request body")

    if key not in g.json_body:
        raise Exception("Missing required parameter '" + key + "'")

    return g.json_body[key]


def optional_param(key):
    if not g.json_body:
        return None

    if key not in g.json_body:
        return None

    return g.json_body[key]


def file_param(key):
    if key in request.files:
        return request.files[key]
    raise Exception("File not present in the request")


@app.before_request
def init_mongo():
    g.mongo = MongoClient(ConfigService.get_mongo_host(), 27017).food_recipes


@app.before_request
def unwind_json():
    g.json_body = request.get_json(force=True, silent=True)


@app.route("/api", methods=["GET"])
def get_hello():
    return jsonify({'admin': 'hello'})


@app.route("/api/image", methods=["POST"])
def post_image():
    return jsonify(ImageService.post_image(file_param('image')))


@app.route("/api/recipe", methods=["GET"])
def get_recipe():
    return RecipeService.get_recipe()


@app.route("/api/recipe", methods=["POST"])
def post_recipe():
    return jsonify(RecipeService.post_recipe(required_param("diet"),
                                             required_param("diet_type"),
                                             required_param("category"),
                                             required_param("dish_type"),
                                             required_param("dish_name"),
                                             required_param("variation"),
                                             required_param("macro_ingredient"),
                                             required_param("chef_name"),
                                             required_param("procedure"),
                                             required_param("macros"),
                                             required_param("images")
                                             ))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
