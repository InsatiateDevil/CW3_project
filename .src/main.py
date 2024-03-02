from utils import load_json, filtered_and_sorted

PATH_TO_OPERATIONS = '../operations.json'


def main():
    list_operations = load_json.load_json(PATH_TO_OPERATIONS)
    list_for_print = filtered_and_sorted.get_filtered_and_sorted_list(list_operations)
    for operation in list_for_print[-5:]:
        date = operation['date'][:10].replace('-', '.')
        description = operation['description']
        if operation.get('from'):
            from_info = operation['from']
        else:
            from_info = None
        to_info = operation['to']
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f"{date} {description}")
        if from_info:
            print(f"{from_info} -> {to_info}")
        else:
            print(f"{to_info}")
        print(f"{amount} {currency}\n")


# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

main()
