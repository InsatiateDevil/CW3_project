from src.main import main


def test_main(list_with_dict):
    assert main() is None
