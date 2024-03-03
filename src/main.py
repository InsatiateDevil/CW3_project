from utils.load_json import load_json
from utils.check_source import print_source_correct
from utils.filtered_and_sorted import get_filtered_and_sorted_list

PATH_TO_OPERATIONS = '../operations.json'


def main():
    list_operations = load_json(PATH_TO_OPERATIONS)
    list_for_print = get_filtered_and_sorted_list(list_operations)
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
            print(f"{print_source_correct(from_info)} -> {print_source_correct(to_info)}")
        else:
            print(f"{print_source_correct(to_info)}")
        print(f"{amount} {currency}\n")


if __name__ == "__main__":
    main()
