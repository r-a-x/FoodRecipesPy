import random

import os

PATH = "images/"


def get_image_path(name):
    return PATH + name


def get_image_name(initial_name):
    return str(random.randint(1000, 9999)) + initial_name


def store_image(image):
    name = get_image_name(image.filename)
    try:
        image.save(os.path.join(PATH, name))
        return True, PATH + name
    except Exception as e:
        print(e)
        return False, None
