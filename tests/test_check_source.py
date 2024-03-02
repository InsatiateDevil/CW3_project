from utils import check_source


def test_check_source(list_with_dict):
    assert check_source.print_source_correct(list_with_dict[0]['from']) == "Maestro 1308 79** **** 7170"
    assert check_source.print_source_correct(list_with_dict[0]['to']) == "Счет **8612"
