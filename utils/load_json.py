import json


def load_json(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        response = json.load(file)
    return response
