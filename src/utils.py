import json
from datetime import datetime


def load_json(path_to_file):
    """
    :param path_to_file: содержит путь к файлу json, который распаковывается в переменную
    :return: возвращает переменную с содержимым файла json
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        response = json.load(file)
    return response


def get_filtered_list(list_with_dict):
    """
    :param list_with_dict: Содержит список со словарями, содержащими информацию о банковских операциях
    :return: список, содержащий только успешные операции, а также он уже отсортирован по дате/времени
    """
    filtered_list = []
    for dictionary in list_with_dict:
        if dictionary.get('state') == 'EXECUTED':
            filtered_list.append(dictionary)
    return filtered_list


def get_sorted_list(list_with_dict):
    """
    :param list_with_dict: лист для сортировки, содержит внутри словари
    :return: лист отсортированный по дате внутри словарей, из которых создает
    """
    return sorted(list_with_dict, key=lambda x: x['date'], reverse=True)


def print_source_correct(info_about_source):
    """
    :param info_about_source: содержит строку с описанием источника(карта или счет) и его номер
    :return: готовое, отредактированное сообщение с замаскированными элементами номера
    """
    if info_about_source[0:4] == "Счет":
        return f"Счет **{info_about_source[-4:]}"
    else:
        number = info_about_source[-16:]
        first_block = f"{number[:4]}"
        second_block = f"{number[4:6]}**"
        third_block = "****"
        fourth_block = f"{number[-4:]}"
        return f"{info_about_source[:-16]}{first_block} {second_block} {third_block} {fourth_block}"


def print_from_dict(about_operation):
    """
    :param about_operation: содержит словарь с информацией о одной операции
    :return: None(занимается непосредственно принтом)
    """
    date = datetime.fromisoformat(about_operation['date'])
    date = date.strftime('%d.%m.%Y')
    description = about_operation['description']
    from_info = about_operation.get('from')
    to_info = about_operation['to']
    amount = about_operation['operationAmount']['amount']
    currency = about_operation['operationAmount']['currency']['name']
    print(f"{date} {description}")
    if from_info:
        print(f"{print_source_correct(from_info)} -> {print_source_correct(to_info)}")
    else:
        print(f"{print_source_correct(to_info)}")
    print(f"{amount} {currency}\n")
