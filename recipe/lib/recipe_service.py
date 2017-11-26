import os
from flask import g
from bson.json_util import dumps


class RecipeService:
    def __init__(self):
        pass

    @staticmethod
    def get_recipe():
        collection = g.mongo.recipe.find({})
        return dumps(collection)

    @staticmethod
    def post_recipe(diet,
                    diet_type,
                    category,
                    dish_type,
                    dish_name,
                    variation,
                    macro_ingredient,
                    chef_name,
                    procedure,
                    macros,
                    images):
        recipe_id = g.mongo.recipe.insert_one({"diet": diet,
                                               "diet_type": diet_type,
                                               "category": category,
                                               "dish_type": dish_type,
                                               "dish_name": dish_name,
                                               "variation": variation,
                                               "macro_ingredient": macro_ingredient,
                                               "chef_name": chef_name,
                                               "procedure": procedure,
                                               "macros": macros,
                                               "images": images})
        return {"recipe_id": str(recipe_id.inserted_id),
                "diet": diet,
                "diet_type": diet_type,
                "category": category,
                "dish_type": dish_type,
                "dish_name": dish_name,
                "variation": variation,
                "macro_ingredient": macro_ingredient,
                "chef_name": chef_name,
                "procedure": procedure,
                "macros": macros,
                "images": images}

    @staticmethod
    def post_recipes_unprocessed(diet,
                                 diet_type,
                                 category,
                                 dish_type,
                                 dish_name,
                                 variation,
                                 macro_ingredient,
                                 chef_name,
                                 macros,
                                 text_dump,
                                 images):
        pass
