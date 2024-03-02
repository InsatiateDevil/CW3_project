def get_filtered_and_sorted_list(list_with_dict):
    filtered_list = []
    for dictionary in list_with_dict:
        if dictionary:
            if dictionary['state'] == 'EXECUTED':
                filtered_list.append(dictionary)
    filtered_and_sorted_list = sorted(filtered_list, key=lambda x: x['date'])
    return filtered_and_sorted_list
