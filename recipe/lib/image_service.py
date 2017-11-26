from lib import image_path_generator


class ImageService:
    def __init__(self):
        pass

    @staticmethod
    def get_image():
        pass

    @staticmethod
    def post_image(image):
        status, path = image_path_generator.store_image(image)
        return {"path": str(path)}
