import pytest
import json


@pytest.fixture
def list_with_dict():
    return json.load(open("operations_for_tests.json"))
