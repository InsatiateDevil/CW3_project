from src import main


def test_main(list_with_dict):
    assert main.main() is None
