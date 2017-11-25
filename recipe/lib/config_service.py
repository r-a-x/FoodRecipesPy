import os


class ConfigService:
    def __init__(self):
        pass

    @staticmethod
    def get_env_variable(key):
        try:
            return os.environ[key]
        except Exception as _:
            return None

    @staticmethod
    def get_recipe_api_root():
        return ConfigService.get_env_variable("RECIPE_API") or "http://localhost:5000"

    @staticmethod
    def get_mongo_host():
        return ConfigService.get_env_variable("MONGO_HOST") or "localhost"
