import json


def load_json(path_to_file):
    """
    :param path_to_file: содержит путь к файлу json, который распаковывается в переменную
    :return: возвращает переменную с содержимым файла json
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        response = json.load(file)
    return response
