def get_filtered_and_sorted_list(list_with_dict):
    """
    :param list_with_dict: Содержит список со словарями, содержащими информацию о банковских операциях
    :return: список, содержащий только успешные операции, а также он уже отсортирован по дате/времени
    """
    filtered_list = []
    for dictionary in list_with_dict:
        if dictionary:
            if dictionary['state'] == 'EXECUTED':
                filtered_list.append(dictionary)
    filtered_and_sorted_list = sorted(filtered_list, key=lambda x: x['date'])
    return filtered_and_sorted_list
