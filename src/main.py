import os
from utils import load_json, print_from_dict, get_sorted_list
from utils import get_filtered_list

PATH_TO_OPERATIONS = os.path.join(os.path.dirname(__file__), "operations.json")


def main():
    list_operations = load_json(PATH_TO_OPERATIONS)
    filtered_list = get_filtered_list(list_operations)
    sorted_list = get_sorted_list(filtered_list)
    for operation in sorted_list[:5]:
        print_from_dict(operation)


if __name__ == "__main__":
    main()
